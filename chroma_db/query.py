import chromadb
from chromadb.utils import embedding_functions
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PERSIST_DIR = os.path.join(BASE_DIR, "db")

# Connect to persistent ChromaDB client
client = chromadb.PersistentClient(path=PERSIST_DIR)

# Embedding function
embedding_function = embedding_functions.DefaultEmbeddingFunction()

# Get collection (docs)
collection = client.get_collection(
    name="docs",
    embedding_function=embedding_function
)

def query_chromadb(query_text, top_k=2):
    """
    Query ChromaDB collection with given text and return top_k results.
    """
    results = collection.query(
        query_texts=[query_text],
        n_results=top_k
    )
    # Return only documents for simplicity
    return results["documents"][0]

# For testing (optional)
if __name__ == "__main__":
    test_query = "What is ChromaDB?"
    print("🔍 Test Results:", query_chromadb(test_query, 2))
