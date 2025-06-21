from transformers import (
    pipeline,
)  # this line imports the pipeline function for using pre-trained models
from transformers.pipelines import (
    PipelineException,
)  # this line imports the PipelineException for handling errors in the pipeline


def generate_text(prompt):
    print("🤖 AI is thinking...\n")
    try:
        gen = pipeline("text-generation", model="gpt2")
        result = gen(
            f"Answer the term in detail with simple language and clearly: {prompt}",
            max_length=50,
            num_return_sequences=1,
        )
        return result[0]["generated_text"]
    except PipelineException:
        return "⚠️ Error: Model pipeline could not be created."
    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"


if __name__ == "__main__":
    print(
        "👋 Hello! I’m your AI assistant using Hugging Face GPT-2. Type 'exit' to quit."
    )
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        output = generate_text(prompt)
        print("🤖 AI:", output.strip())


# NOTE: transformers library is a powerful tool for working with pre-trained models, and it can be used as an alternative to OpenAI's API for text generation tasks.
# It allows you to run models locally, which can be beneficial for privacy and cost reasons.
# However, it may not have the same level of performance or capabilities as OpenAI's models.
# Make sure to install the transformers library
# using `pip install transformers` before running this code.
# also its recommended to install  `torch` or `tensorflow` as a backend for transformers. Backend here refers to the underlying framework that the transformers library uses to run the models.
# For example, you can install PyTorch with `pip install torch` or TensorFlow with `pip install tensorflow`.
# nowadays PyTorch is more commonly used with transformers, so you might want to install it if you haven't already over the tensorflow. because PyTorch has better support and performance for most transformer models.
