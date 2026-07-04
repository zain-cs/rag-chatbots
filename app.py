import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from src.pdf_loader import load_document

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 RAG Chatbot")
st.caption("Powered by GPT-2 — Ask questions about any document!")

# ── Load Model ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
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

                # Generate answer
                prompt = f"Based on this information: {chunk}\nQuestion: {question}\nAnswer:"
                inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=400, truncation=True)
                with torch.no_grad():
                    outputs = model.generate(
                        inputs,
                        max_new_tokens=60,
                        do_sample=True,
                        temperature=0.7,
                        top_p=0.9,
                        repetition_penalty=1.3,
                        pad_token_id=tokenizer.eos_token_id,
                        eos_token_id=tokenizer.eos_token_id,
                    )
                generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
                answer = generated.split("Answer:")[-1].strip().split('\n')[0].strip()
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
else:
    st.info("👆 Please upload a TXT or PDF file to get started!")