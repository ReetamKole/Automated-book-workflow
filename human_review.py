import os

def edit_in_editor(filepath="output/ai_reviewer_output.txt"):
    print(f"🔍 Opening {filepath} in Notepad...")
    if os.path.exists(filepath):
        os.system(f'notepad "{filepath}"')
    else:
        print("❌ File not found.")
