import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def ask_gemini(prompt):
    try:
        print("🤖 Thinking...\n")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


if __name__ == "__main__":
    print("👋 Hello! I’m your AI-powered virtual assistant. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        reply = ask_gemini(user_input)
        print("🤖 AI:", reply, "\n")
