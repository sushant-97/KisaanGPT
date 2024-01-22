# KisaanGPT
### RAG Pipeline Documentation

## Overview
The RAG (Retrieval-Augmented Generation) pipeline is a system designed for efficient information retrieval and processing. It utilizes advanced embedding and reranking techniques to enhance the quality and relevance of search results. This documentation provides an overview of the pipeline's components and usage.



## Install required libraries
```
pip install -r requirements.txt
```
## Dataset Preprocssing
Download the dataset from google [drive link](https://drive.google.com/drive/folders/18AYK3HDOJBxJxXC_wpabgTnmv4fJUix7?usp=sharing) and preprocess as per preprocess.ipynb file

## Components
The pipeline consists of several key components:

### 1. LLMEmbedder and FlagReranker
- `LLMEmbedder` and `FlagReranker` are central to the pipeline, handling the embedding of queries and reranking of search results respectively.
- These models are initialized in both `searchdb.py` and `main.py` scripts.

### 2. Data Loading and Processing
- The `searchdb.py` script includes functionality to load and process datasets, preparing them for retrieval tasks.

### 3. Flask Web Application
- `main.py` sets up a Flask-based web application, providing an API endpoint for handling retrieval requests.

## Usage
To use the ABVE RAG pipeline, follow these steps:

1. **Initialize the Models**: Ensure that the `LLMEmbedder` and `FlagReranker` models are correctly initialized with the required configurations.

2. **Load and Process Data**: Use the functionality in `searchdb.py` to load and process your dataset for retrieval tasks.

3. **Run the Flask App**: Start the Flask application in `main.py` to enable the API endpoint.

4. **Query the API**: Send POST requests to the `/openrouter-query` endpoint with your queries to receive ranked search results.

## API Endpoint
- URL: `/openrouter-query`
- Method: POST
- Description: Handles incoming search queries and returns ranked results.

## Conclusion
The RAG pipeline is a powerful tool for enhancing search and retrieval tasks with advanced embedding and reranking capabilities. Its Flask-based web application makes it easily accessible for various applications.


# Integration with KisaanGPT Web Application

The RAG pipeline API can be effectively integrated into the KisaanGPT web application in the following ways:

### 1. Integration with "Start Asking" Button in `index.html`
- The "Start Asking" button on the home page (`index.html`) can be linked to the ABVE RAG pipeline API.
- When a user clicks this button, it can open a dialogue interface where users can type in their queries.
- The queries can then be sent to the ABVE RAG pipeline API, and the responses displayed to the user.

### 2. Integration in Interactive Sessions in `kisaanGPT.html`
- The `kisaanGPT.html` page contains interactive elements like "Start New Session" buttons.
- These sessions can be designed to accept user queries related to agricultural topics.
- Each query can be processed by the RAG pipeline API, providing users with relevant and accurate information.

### 3. General Usage in Web Application
- The RAG pipeline API can be used as a backend service for the KisaanGPT application, enhancing its capability to provide real-time, accurate responses to user queries.
