from chromadb_manager import save_version

# Save final version
with open("output/final_version.txt", "r", encoding="utf-8") as f:
    final_text = f.read()
save_version("final_version", final_text)

# Save writer output
with open("output/ai_writer_output.txt", "r", encoding="utf-8") as f:
    writer_text = f.read()
save_version("ai_writer_output", writer_text)

# Save reviewer output
with open("output/ai_reviewer_output.txt", "r", encoding="utf-8") as f:
    reviewer_text = f.read()
save_version("ai_reviewer_output", reviewer_text)

print("✅ All versions saved to ChromaDB.")
