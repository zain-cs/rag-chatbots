<<<<<<< HEAD
<div align="center">

# 🤖 RAG Chatbot

**Ask questions about any document — get instant AI-powered answers.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

</div>

---

## 📌 Overview

A **RAG (Retrieval-Augmented Generation)** chatbot that answers questions based on the content of any document. Supports both **PDF and TXT** files. Runs completely locally — no API key needed.

> **Core idea: Upload your document. Ask it anything. Get instant answers.**

---

## ✨ Features

- 📄 **PDF & TXT Support** — Upload any document format
- 🌐 **Web UI** — Clean Streamlit interface
- 💻 **CLI Mode** — Terminal-based chat
- 🔒 **100% Local** — No API key or internet required
- ⚡ **Fast** — GPT-2 runs on CPU

---

## 🖥️ Web Interface

Run the web app and chat with your documents through a clean browser UI:

```bash
streamlit run app.py
```

---

## 💬 Sample Conversation

```
📄 Document: AI & Machine Learning Guide

You: What is machine learning?
🤖 Bot: Machine learning is a subset of AI that allows systems to learn from data without being explicitly programmed.

You: What are the types of AI?
🤖 Bot: Narrow AI, General AI, and Super AI.

You: What is TensorFlow?
🤖 Bot: TensorFlow is an open source framework by Google for building machine learning models.
```

---

## 🔍 How RAG Works

```
Your Document (PDF or TXT)
          │
          ▼
Chunk the document into paragraphs
          │
          ▼
Find most relevant chunk for the question (keyword matching)
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
git clone https://github.com/zain-cs/rag-chatbots.git
cd rag-chatbots
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

**4a. Run the Web UI**
```bash
streamlit run app.py
```

**4b. Run the CLI chatbot**
```bash
python src/chatbot.py
```

---

## 🗂️ Project Structure

```
📦 rag-chatbots
┣ 📂 data
┃ ┗ 📄 sample.txt         ← Sample document
┣ 📂 src
┃ ┣ 🐍 chatbot.py         ← CLI chatbot
┃ ┗ 🐍 pdf_loader.py      ← PDF & TXT loader
┣ 🐍 app.py               ← Streamlit web UI
┣ 📄 .gitignore
┣ 📄 requirements.txt
┗ 📄 README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| GPT-2 | Local text generation model |
| HuggingFace Transformers | Model loading and inference |
| PyTorch | Deep learning backend |
| Streamlit | Web UI framework |
| PyMuPDF | PDF text extraction |

---

## 🗺️ Roadmap

- [x] Document loading and chunking
- [x] Keyword-based relevant chunk retrieval
- [x] GPT-2 local text generation
- [x] Interactive CLI chat loop
- [x] PDF & TXT support
- [x] Streamlit web interface
- [ ] Semantic search with embeddings
- [ ] Upgrade to Gemini or GPT-4 API
- [ ] Deploy on Hugging Face Spaces

---

## 👤 Author

**Zain** — [@zain-cs](https://github.com/zain-cs)

> Open to freelance ML and AI projects.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and build on it.
=======
---
title: Rag Chatbot
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: RAG Chatbot that answers questions about any PDF or TXT
license: mit
---

# Welcome to Streamlit!

Edit `/src/streamlit_app.py` to customize this app to your heart's desire. :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
>>>>>>> 8b93c6ff8d7b1002ed1d53227d23920e4b4c423a
