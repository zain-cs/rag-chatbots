---
title: Rag Chatbot
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: RAG Chatbot that answers questions about any PDF or TXT
license: mit
---

<div align="center">

# 🤖 RAG Chatbot

**Ask questions about any document — get instant AI-powered answers.**

[![Live Demo](https://img.shields.io/badge/🤗%20Live%20Demo-Hugging%20Face%20Spaces-blue?style=flat-square)](https://huggingface.co/spaces/zain-cs/rag-chatbot)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

**🔗 [Try it live](https://huggingface.co/spaces/zain-cs/rag-chatbot) — no install needed**

</div>
---

<div align="center">
  <img src="assets/demo.png" alt="RAG Chatbot Demo" width="700">
</div>

---

## 📌 Overview

A **RAG (Retrieval-Augmented Generation)** chatbot that answers questions based on the content of any document. Supports both **PDF and TXT** files, uses **semantic search** (via sentence-transformers) to find the most relevant context, and generates answers using **Flan-T5**, an instruction-tuned model that paraphrases rather than copying text verbatim. Deployed live on Hugging Face Spaces with Docker — no API key needed.

> **Core idea: Upload your document. Ask it anything. Get instant answers.**

---

## ✨ Features

- 📄 **PDF & TXT Support** — Upload any document format
- 🧠 **Semantic Search** — Finds relevant context using sentence embeddings, not just keyword matching
- 🌐 **Web UI** — Clean Streamlit interface, live on Hugging Face Spaces
- 💻 **CLI Mode** — Terminal-based chat, for local/offline use
- 🐳 **Dockerized Deployment** — Fully containerized and reproducible
- 🔒 **Self-contained** — No external API key required to run

---

## 🚀 Live Demo

**[huggingface.co/spaces/zain-cs/rag-chatbot](https://huggingface.co/spaces/zain-cs/rag-chatbot)**

Upload a PDF or TXT file, then ask questions about its content directly in your browser.

---

## 🖥️ Running Locally

**1. Clone the repository**
```bash
git clone https://github.com/zain-cs/rag-chatbots.git
cd rag-chatbots
```

**2. Create and activate a virtual environment**
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

## 🔍 How RAG Works

```
Your Document (PDF or TXT)
          │
          ▼
Chunk the document into passages
          │
          ▼
Embed chunks + question with sentence-transformers
          │
          ▼
Retrieve the most semantically relevant chunk
          │
          ▼
Feed chunk + question to Flan-T5
          │
          ▼
Generated Answer
```

---

## 🗂️ Project Structure

```
📦 rag-chatbots
┣ 📂 data
┃ ┗ 📄 sample.txt              ← Sample document
┣ 📂 src
┃ ┣ 🐍 chatbot.py              ← CLI chatbot
┃ ┣ 🐍 pdf_loader.py           ← PDF & TXT loader
┃ ┗ 🐍 semantic_search.py      ← Embedding-based chunk retrieval
┣ 🐍 app.py                    ← Streamlit web UI (deployed entry point)
┣ 🐳 Dockerfile                ← Container config for Hugging Face Spaces
┣ 📄 .gitignore
┣ 📄 requirements.txt
┗ 📄 README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Flan-T5 (base) | Local instruction-tuned text generation model |
| Sentence-Transformers (MiniLM) | Semantic embeddings for retrieval |
| HuggingFace Transformers | Model loading and inference |
| PyTorch | Deep learning backend |
| Streamlit | Web UI framework |
| PyMuPDF | PDF text extraction |
| Docker | Containerized deployment |

---

## 🗺️ Roadmap

- [x] Document loading and chunking
- [x] Interactive CLI chat loop
- [x] PDF & TXT support
- [x] Streamlit web interface
- [x] Semantic search with embeddings
- [x] Deploy on Hugging Face Spaces
- [x] Upgrade generation model to Flan-T5 (instruction-tuned) for higher answer quality
- [ ] Experiment with larger models (Flan-T5-large or an API-based LLM) for even better answer quality

---

## 👤 Author

**Zain** — [@zain-cs](https://github.com/zain-cs)

> Open to freelance ML and AI projects.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and build on it.
