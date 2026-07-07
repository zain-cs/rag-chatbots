from sentence_transformers import SentenceTransformer
import numpy as np


def get_semantic_chunk(question: str, document: str, top_k: int = 3) -> str:
    """
    Find the most relevant chunk(s) from document using semantic search.

    Args:
        question: User's question.
        document: Full document text.
        top_k: Number of top-matching paragraphs to combine for context.

    Returns:
        Combined text of the most semantically relevant paragraphs.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Split into raw lines first
    raw_lines = [p.strip() for p in document.split('\n') if p.strip()]

    # Merge short lines (e.g. headings) with the line(s) that follow them,
    # so a heading and its explanation stay together in one chunk.
    paragraphs = []
    buffer = ""
    for line in raw_lines:
        buffer = f"{buffer} {line}".strip() if buffer else line
        if len(buffer) > 150:
            paragraphs.append(buffer)
            buffer = ""
    if buffer:
        paragraphs.append(buffer)

    # Filter out anything still too short to be useful
    paragraphs = [p for p in paragraphs if len(p) > 30]

    if not paragraphs:
        return document[:500]

    # Encode question and paragraphs
    question_embedding = model.encode([question])
    paragraph_embeddings = model.encode(paragraphs)

    # Calculate cosine similarity
    similarities = np.dot(
        paragraph_embeddings, question_embedding.T
    ).flatten()

    # Return top_k most similar paragraphs, combined in original order
    top_k = min(top_k, len(paragraphs))
    top_indices = np.argsort(similarities)[-top_k:]
    top_indices_sorted = sorted(top_indices)  # preserve document order

    combined = "\n\n".join(paragraphs[i] for i in top_indices_sorted)
    return combined
