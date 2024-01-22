from FlagEmbedding import LLMEmbedder, FlagReranker 
import os
import lancedb
import re
import pandas as pd
import random

from datasets import load_dataset

import torch
import gc

import lance
from lancedb.embeddings import with_embeddings


task = "qa" # Encode for a specific task (qa, icl, chat, lrlm, tool, convsearch)
embed_model = LLMEmbedder('BAAI/llm-embedder', use_fp16=False) # Load model (automatically use GPUs)

reranker_model = FlagReranker('BAAI/bge-reranker-base', use_fp16=True) # use_fp16 speeds up computation with a slight performance degradation




"""# Load `Chunks` of data from [BeIR Dataset](https://huggingface.co/datasets/BeIR/scidocs)

Note: This is a dataset built specially for retrieval tasks to see how good your search is working
"""
data=pd.read_csv("Kcc_subset.csv")

 # just random samples for faster embed demo
data['documents'] = 'query:' + data['QueryText'] + ', answer:' + data['KccAns']
data = data.dropna()
def embed_documents(batch):
    """
    Function to embed the whole text data
    """
    return embed_model.encode_keys(batch, task=task) # Encode data or 'keys'


db = lancedb.connect("./db") # Connect Local DB
if "doc_embed" in db.table_names():
  table = db.open_table("doc_embed") # Open Table
else:
  # Use the train text chunk data to save embed in the DB
  data1 = with_embeddings(embed_documents, data, column = 'documents',show_progress = True, batch_size = 512)
  table = db.create_table("doc_embed", data=data1) # create Table

"""# Search from a random Text"""

def search(query, top_k = 10):
  """
  Search a query from the table
  """
  query_vector = embed_model.encode_queries(query, task=task) # Encode the QUERY (it is done differently than the 'key')
  search_results = table.search(query_vector).limit(top_k)
  return ",".join(search_results.to_pandas().dropna(subset = "QueryText").reset_index(drop = True)["documents"].to_list())


# query = "how to control flower drop in bottelgourd?"
# print("QUERY:-> ", query)

# # get top_k search results
# search_results = search(query, top_k = 10).to_pandas().dropna(subset = "Query").reset_index(drop = True)["documents"]
# print(",".join(search_results.to_list))
# def rerank(query, search_results):
#   search_results["old_similarity_rank"] = search_results.index+1 # Old ranks

#   torch.cuda.empty_cache()
#   gc.collect()

#   search_results["new_scores"] = reranker_model.compute_score([[query,chunk] for chunk in search_results["text"]]) # Re compute ranks
#   return search_results.sort_values(by = "new_scores", ascending = False).reset_index(drop = True)

# print("QUERY:-> ", query)