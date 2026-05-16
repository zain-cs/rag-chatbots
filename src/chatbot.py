from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import warnings
warnings.filterwarnings('ignore')

# ── 1. Load Model ─────────────────────────────────────────────────────────────
print("⏳ Loading AI model...")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
print("✅ Model loaded!\n")

# ── 2. Load Document ──────────────────────────────────────────────────────────
with open("data/sample.txt", 'r', encoding='utf-8') as f:
    document = f.read()
print(f"✅ Document loaded! {len(document.split())} words\n")

# ── 3. Find relevant chunk ────────────────────────────────────────────────────
def get_relevant_chunk(question, doc):
    question_words = set(question.lower().split())
    paragraphs = [p.strip() for p in doc.split('\n') if len(p.strip()) > 30]
    best, best_score = "", 0
    for para in paragraphs:
        score = len(question_words & set(para.lower().split()))
        if score > best_score:
            best_score = score
            best = para
    return best if best else doc[:300]

# ── 4. Answer Function ────────────────────────────────────────────────────────
def ask(question, doc):
    chunk = get_relevant_chunk(question, doc)
    prompt = f"Based on this information: {chunk}\nQuestion: {question}\nAnswer:"
    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=400, truncation=True)
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_new_tokens=60,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    answer = generated.split("Answer:")[-1].strip()
    return answer.split('\n')[0].strip()

# ── 5. Chat Loop ──────────────────────────────────────────────────────────────
print("🤖 RAG Chatbot — Powered by GPT-2 (Local AI)")
print("📄 Answering questions about: AI & Machine Learning")
print("─" * 50)
print("Type 'quit' to exit\n")

while True:
    question = input("You: ").strip()
    if not question:
        continue
    if question.lower() in ['quit', 'exit', 'q']:
        print("Goodbye! 👋")
        break
    answer = ask(question, document)
    print(f"\n🤖 Bot: {answer}\n")