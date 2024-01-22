# KisaanGPT
### RAG Pipeline Documentation

## Overview
The RAG (Retrieval-Augmented Generation) pipeline is a system designed for efficient information retrieval and processing. It utilizes advanced embedding and reranking techniques to enhance the quality and relevance of search results. This documentation provides an overview of the pipeline's components and usage.

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
