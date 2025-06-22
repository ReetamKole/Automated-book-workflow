from ai_writer import spin_chapter

with open("output/chapter.txt", "r", encoding="utf-8") as f:
    original_text = f.read()

# First rewrite by AI Writer
writer_output = spin_chapter(original_text, role="AI Writer")

# Review pass by AI Reviewer
reviewer_output = spin_chapter(writer_output, role="AI Reviewer")

# Save outputs
with open("output/ai_writer_output.txt", "w", encoding="utf-8") as f:
    f.write(writer_output)

with open("output/ai_reviewer_output.txt", "w", encoding="utf-8") as f:
    f.write(reviewer_output)

print("✅ Writer and Reviewer outputs saved in /output.")

# from human_review import edit_in_editor

# # Open AI-reviewed version in Notepad for manual edit
# edit_in_editor("output/ai_reviewer_output.txt")

# # After edit, load the final version
# with open("output/ai_reviewer_output.txt", "r", encoding="utf-8") as f:
#     final_version = f.read()

# # Save final version (optionally with timestamp)
# with open("output/final_version.txt", "w", encoding="utf-8") as f:
#     f.write(final_version)

# print("\n✅ Final version saved to output/final_version.txt")

import os

def choose_and_finalize_version():
    print("\n📝 Preview options:")
    print("1. View AI Writer Output")
    print("2. View AI Reviewer Output")
    print("3. Edit AI Writer Output")
    print("4. Edit AI Reviewer Output")
    print("5. Use AI Writer Output without editing")
    print("6. Use AI Reviewer Output without editing")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        os.system('notepad "output/ai_writer_output.txt"')
        return choose_and_finalize_version()

    elif choice == "2":
        os.system('notepad "output/ai_reviewer_output.txt"')
        return choose_and_finalize_version()

    elif choice == "3":
        os.system('notepad "output/ai_writer_output.txt"')
        selected_file = "output/ai_writer_output.txt"

    elif choice == "4":
        os.system('notepad "output/ai_reviewer_output.txt"')
        selected_file = "output/ai_reviewer_output.txt"

    elif choice == "5":
        selected_file = "output/ai_writer_output.txt"

    elif choice == "6":
        selected_file = "output/ai_reviewer_output.txt"

    else:
        print("❌ Invalid choice. Defaulting to reviewer output.")
        selected_file = "output/ai_reviewer_output.txt"

    # Save the final version
    with open(selected_file, "r", encoding="utf-8") as src, \
         open("output/final_version.txt", "w", encoding="utf-8") as dst:
        dst.write(src.read())

    print("✅ Final version saved to output/final_version.txt")

# Run the version selector
choose_and_finalize_version()

from chromadb_manager import save_version

# Load all version contents
with open("output/ai_writer_output.txt", "r", encoding="utf-8") as f:
    writer = f.read()
with open("output/ai_reviewer_output.txt", "r", encoding="utf-8") as f:
    reviewer = f.read()
with open("output/final_version.txt", "r", encoding="utf-8") as f:
    final = f.read()

# Save all versions to ChromaDB
save_version("chapter1-writer", writer, {"source": "AI Writer"})
save_version("chapter1-reviewer", reviewer, {"source": "AI Reviewer"})
save_version("chapter1-final", final, {"source": "Human Final"})
