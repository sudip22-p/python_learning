import os
from dotenv import load_dotenv
from openai import OpenAI
from openai import RateLimitError, APIConnectionError, AuthenticationError, OpenAIError

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("⚠️  API key is missing. Please check your setup.")
    exit()

client = OpenAI(api_key=api_key)


def chat_with_openai(message):
    print("🤖 AI is thinking...\n")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            max_tokens=100,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        return "⚠️ Your usage limit has been reached. Please upgrade your OpenAI plan or try again later."
    except AuthenticationError:
        return "⚠️ Your API key is invalid. Please double-check your `.env` file."
    except APIConnectionError:
        return (
            "⚠️ Unable to reach OpenAI servers. Please check your internet connection."
        )
    except OpenAIError:
        return "⚠️ Something went wrong while processing your request. Please try again later."
    except Exception:
        return "⚠️ Unexpected error occurred. Please try again."


if __name__ == "__main__":
    print("👋 Hello! I’m your AI assistant. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        reply = chat_with_openai(user_input)
        print("🤖 AI:", reply)

# NOTE: This AI sometimes stop working coz of rate limit, so using  the HuggingFace Transformers library as an alternative in next file.
