import os
import google.generativeai as genai

# Set up Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def spin_chapter(text, role="AI Writer"):
    prompt = f"{role}: Rewrite the following chapter to improve storytelling while keeping the original meaning and sequence. Be creative, concise, and engaging.\n\n{text}"

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Gemini Error:", e)
        return ""
