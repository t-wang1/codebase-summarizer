import chromadb
from langchain.embeddings.openai import OpenAIEmbeddings


chroma_client = chromadb.PersistentClient(path="code_db") # initializes persistent vector database 
collection = chroma_client.get_or_create_collection(name="codebase")

def store_codebase_embeddings(code_structure):
    embeddings = OpenAIEmbeddings()

    for file_info in code_structure:
        text = f"File: {file_info['file']}\n Classes: {file_info['classes']}\n Functions: {file_info['functions']}\n Imports: {file_info['imports']}"
        vector = embeddings.embed_query(text)
        collection.add(ids=file_info['file'], embeddings=vector, metadate=[file_info])

def query_codebase(query):
    results = collection.query(query_text=query, n_results=3) # retrieves top 3 files after querying
    return results['metadatas']