from chromadb_manager import collection

print("🧾 Total documents stored:", collection.count())
print("🆔 Stored document IDs:", collection.get()["ids"])
