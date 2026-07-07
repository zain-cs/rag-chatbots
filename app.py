import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from src.pdf_loader import load_document

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 RAG Chatbot")
st.caption("Powered by Flan-T5 — Ask questions about any document!")

# ── Load Model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
    return tokenizer, model

with st.spinner("⏳ Loading AI model..."):
    tokenizer, model = load_model()
st.success("✅ Model loaded!")

# ── File Upload ───────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "📂 Upload your document",
    type=["txt", "pdf"]
)

if uploaded_file:
    # Save temporarily
    with open(f"data/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    document = load_document(f"data/{uploaded_file.name}")
    st.success(f"✅ Document loaded! {len(document.split())} words")

    # ── Chat ──────────────────────────────────────────────────────────────────
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if question := st.chat_input("Ask a question about your document..."):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Get relevant chunk using semantic search
                from src.semantic_search import get_semantic_chunk
                chunk = get_semantic_chunk(question, document)
                with st.expander("🔍 Debug: Retrieved chunk"):
                    st.write(chunk)

                # Generate answer
                prompt = (
                    f"Using only the information in the context below, write one well-formed, "
                    f"grammatically correct sentence that answers the question. "
                    f"Do not copy the context word-for-word — rephrase it in your own words.\n\n"
                    f"Context: {chunk}\n\n"
                    f"Question: {question}\n\n"
                    f"Answer:"
                )   
                inputs = tokenizer(
                    prompt,
                    return_tensors="pt",
                    max_length=512,
                    truncation=True
                )
                with torch.no_grad():
                    outputs = model.generate(
                        **inputs,
                        max_new_tokens=100,
                        min_new_tokens=20,
                        num_beams=4,
                        early_stopping=True,
                        repetition_penalty=1.3,
                    )
                answer = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
else:
    st.info("👆 Please upload a TXT or PDF file to get started!")
