from sentence_transformers import SentenceTransformer
import numpy as np


def get_semantic_chunk(question: str, document: str) -> str:
    """
    Find the most relevant chunk from document using semantic search.

    Args:
        question: User's question.
        document: Full document text.

    Returns:
        Most semantically relevant paragraph.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Split into paragraphs
    paragraphs = [
        p.strip() for p in document.split('\n')
        if len(p.strip()) > 30
    ]

    if not paragraphs:
        return document[:300]

    # Encode question and paragraphs
    question_embedding = model.encode([question])
    paragraph_embeddings = model.encode(paragraphs)

    # Calculate cosine similarity
    similarities = np.dot(
        paragraph_embeddings, question_embedding.T
    ).flatten()

    # Return most similar paragraph
    best_idx = np.argmax(similarities)
    return paragraphs[best_idx]