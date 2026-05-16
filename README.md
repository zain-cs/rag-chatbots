<div align="center">

# 🤖 RAG Chatbot

**Ask questions about any document — get instant AI-powered answers.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

</div>

---

## 📌 Overview

This project implements a **RAG (Retrieval-Augmented Generation)** chatbot that answers questions based on the content of a document. Instead of relying on general knowledge, the bot finds the most relevant section of your document and generates a focused answer.

> **Core idea: Feed the AI your document. Ask it anything about it.**

---

## 💬 Sample Conversation

```
📄 Document: AI & Machine Learning Guide

You: What is machine learning?
🤖 Bot: Machine learning is a subset of AI that allows systems
        to learn from data without being explicitly programmed.

You: What are the types of AI?
🤖 Bot: Narrow AI, General AI, and Super AI.

You: What is TensorFlow?
🤖 Bot: TensorFlow is an open source framework by Google
        for building machine learning models.
```

---

## 🔍 How RAG Works

```
Your Document (TXT)
        │
        ▼
Chunk the document into paragraphs
        │
        ▼
Find most relevant chunk for the question
(keyword matching)
        │
        ▼
Feed chunk + question to GPT-2
        │
        ▼
Generated Answer
```

---

## 🚀 Quickstart

**1. Clone the repository**
```bash
git clone https://github.com/zain-cs/rag-chatbot.git
cd rag-chatbot
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the chatbot**
```bash
python src/chatbot.py
```

---

## 🗂️ Project Structure

```
📦 rag-chatbot
 ┣ 📂 data
 ┃ ┗ 📄 sample.txt          ← Document the chatbot answers from
 ┣ 📂 src
 ┃ ┗ 🐍 chatbot.py          ← Main RAG chatbot
 ┣ 📄 .gitignore
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```

---

## 📄 Using Your Own Document

Simply replace `data/sample.txt` with any `.txt` file of your choice:

```
data/
└── your_document.txt   ← paste your own content here
```

Then update this line in `chatbot.py`:

```python
with open("data/your_document.txt", 'r', encoding='utf-8') as f:
```

The chatbot will now answer questions about your document. ✅

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| GPT-2 | Local text generation model |
| HuggingFace Transformers | Model loading and inference |
| PyTorch | Deep learning backend |

---

## 🗺️ Roadmap

- [x] Document loading and chunking
- [x] Keyword-based relevant chunk retrieval
- [x] GPT-2 local text generation
- [x] Interactive chat loop
- [ ] Upgrade to Gemini or GPT-4 API
- [ ] Add PDF support
- [ ] Build Streamlit web interface
- [ ] Semantic search with embeddings

---

## 👤 Author

**Zain** — [@zain-cs](https://github.com/zain-cs)

> Open to freelance ML and AI projects.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and build on it.