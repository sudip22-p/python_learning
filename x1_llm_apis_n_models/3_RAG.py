from transformers import T5Tokenizer, T5ForConditionalGeneration
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Crop-related knowledge base (sample)
crop_docs = [
    "Wheat is a cereal grain grown worldwide.",
    "Rice is a staple food in many countries.",
    "Maize or corn is used for food and biofuel.",
    "Proper irrigation is essential for crop growth.",
    "Fertilizers improve soil nutrient content.",
    "Pests can damage crops and reduce yield.",
    "Crop rotation helps maintain soil health.",
]

# Initialize sentence transformer and encode docs
embedder = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embedder.encode(crop_docs, convert_to_numpy=True)

# Build FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

# Load T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")

# Similarity threshold (experiment and tune this)
SIMILARITY_THRESHOLD = 1.0  # Lower is more similar since using L2 distance


def is_in_domain(query_embedding):
    distances, _ = index.search(query_embedding, 1)
    # FAISS L2 returns squared Euclidean distance
    # Smaller distance = more similar
    return distances[0][0] < SIMILARITY_THRESHOLD


def rag_crop_bot(query, top_k=3):
    query_embedding = embedder.encode([query], convert_to_numpy=True)

    if not is_in_domain(query_embedding):
        return "Sorry, I can only answer crop-related questions."

    distances, indices = index.search(query_embedding, top_k)
    retrieved_docs = [crop_docs[i] for i in indices[0]]

    context = " ".join(retrieved_docs)
    input_text = f"question: {query} context: {context}"

    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_length=100)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer


if __name__ == "__main__":
    print("Crop Info Bot. Ask me anything about crops. Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = rag_crop_bot(query.lower().strip())
        print("Bot:", response)
