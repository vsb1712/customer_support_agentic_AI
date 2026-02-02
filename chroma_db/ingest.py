import chromadb
from chromadb.utils import embedding_functions
import os

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")  # optional: can store .txt files
DB_DIR = os.path.join(BASE_DIR, "db")
os.makedirs(DB_DIR, exist_ok=True)

# --- Connect to persistent ChromaDB ---
client = chromadb.PersistentClient(path=DB_DIR)
embedding_function = embedding_functions.DefaultEmbeddingFunction()

collection = client.get_or_create_collection(
    name="docs",
    embedding_function=embedding_function
)

# --- Example Q&A documents ---
# Each entry can be a small paragraph answering a question
documents = [
    "ChromaDB is a vector database for AI applications.",
    "AWS EC2 is a virtual server in the cloud that can run Linux or Windows.",
    "Python is a popular programming language used for AI, web development, and automation.",
    "Relational databases store structured data in tables and support SQL queries.",
    "Vector databases store embeddings for similarity search in AI applications.",
    "Semantic search allows searching for meaning, not just keywords.",
    "EC2 instances can be scaled vertically or horizontally depending on workload.",
    "ChromaDB can be used to power chatbots, recommendation systems, and RAG pipelines."
]

# --- Assign unique IDs ---
ids = [f"doc_{i}" for i in range(len(documents))]

# --- Add documents to ChromaDB collection ---
collection.add(documents=documents, ids=ids)

print(f"✅ {len(documents)} documents added to ChromaDB collection and persisted at: {DB_DIR}")

# --- Optional: verify ingestion ---
all_docs = collection.get(include=["documents", "ids"])
print("Current documents in collection:", all_docs["documents"])
