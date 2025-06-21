from transformers import pipeline
from transformers.utils import logging
import warnings

# Suppress warnings and info logs
logging.set_verbosity_error()
warnings.filterwarnings("ignore")


def generate_factual_text(prompt):
    print("🤖 AI is thinking...\n")
    try:
        gen = pipeline("text2text-generation", model="google/flan-t5-xl")
        result = gen(
            f"Answer the question concisely and factually: {prompt}", max_length=150
        )
        return result[0]["generated_text"]
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


if __name__ == "__main__":
    print("👋 Hi! I’m your factual AI assistant using FLAN-T5-XL. Type 'exit' to quit.")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        answer = generate_factual_text(prompt)
        print("🤖 AI:", answer.strip())


# Note: While running this code, it will download the FLAN-T5-XL model, which is quite large (around 11GB).
# The model is not working properly giving the wrong answers because it is not trained for conversational tasks.
# For more advanced kinnda ai asistant, we can go for retrieval-augmented generation (RAG) and use a combination of a language model and a knowledge base.
# retrieval-augmented generation (RAG) is a technique that combines the strengths of large language models (LLMs) with external knowledge bases to provide more accurate and contextually relevant responses.
