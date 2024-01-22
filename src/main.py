from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS
from FlagEmbedding import LLMEmbedder, FlagReranker 
from searchdb import search
import lancedb

import pandas as pd

task = "qa" # Encode for a specific task (qa, icl, chat, lrlm, tool, convsearch)
embed_model = LLMEmbedder('BAAI/llm-embedder', use_fp16=False) # Load model (automatically use GPUs)

reranker_model = FlagReranker('BAAI/bge-reranker-base', use_fp16=True) # use_fp16 speeds up computation with a slight performance degradation
db = lancedb.connect("./db")

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/openrouter-query": {"origins": "*"}})


# Replace 'your_api_key_here' with the environment variable where you store the API key
OPENROUTER_API_KEY = "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"
# OPENROUTER_API_KEY = "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"
@app.route('/openrouter-query', methods=['POST'])
def query_openrouter():
    print("hit")
    # Get data from the incoming request
    user_message = request.json.get('message')
    print(user_message)

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        Context=search(user_message,top_k=10)
        print("====================",Context,user_message)
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}"
            },
            data=json.dumps({
                "model": "mistralai/mixtral-8x7b-instruct",
                "messages": [
                    {"role": "user", "content": """You are expert assitant who gives reply from Context.Follow this steps. 
                     Step 1: Check first whether the text is greeting or not if yes then do not use context and keep your reply short nd simple.
                     Step 2: if not then check is it related to Indian Agriculture or Not. if not  do not use given Context do not use context.
                     Step 3: if related to Agriculture then use context only to give reply. 
                     Not all queries are related to agricuture so be smart Also in final answer give suggestion and precutions to take while using perticular chemical,Query:{},Context:{}""".format(user_message,Context)}
                ]
            })
        )

        # Check if the request was successful
        if response.status_code != 200:
            return jsonify({"error": "Failed to get response from OpenRouter"}), 500

        data = response.json()
        print(data)
        result=data["choices"][0]["message"]["content"]
        if("answer" in result):
            result=result.split("answer")
        return jsonify(data["choices"][0]["message"]["content"])

    except Exception as e:
        print("exception", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
