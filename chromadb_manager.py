from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Initialize embedding function
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# ✅ Use persistent client with local storage path
client = PersistentClient(path="./chroma_db")

# Create or get collection with embedding function
collection = client.get_or_create_collection(
    name="chapter_versions",
    embedding_function=embedding_function
)

def save_version(doc_id, content, metadata=None):
    if metadata is None:
        metadata = {"source": "unknown"}

    collection.add(
        documents=[content],
        ids=[doc_id],
        metadatas=[{"version_name": doc_id, **metadata}]
    )
    print(f"✅ Saved version '{doc_id}' to ChromaDB.")

def search_version(query, n_results=1):
    results = collection.query(query_texts=[query], n_results=n_results)
    docs = results.get("documents", [])
    ids = results.get("ids", [])
    if docs and docs[0]:
        return ids[0][0], docs[0][0]
    else:
        return None, None

