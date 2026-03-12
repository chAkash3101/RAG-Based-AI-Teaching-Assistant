
# 🎓 RAG-Based AI Teaching Assistant

A fully offline RAG (Retrieval-Augmented Generation) pipeline that lets you 
ask natural language questions about video lectures and get pointed to the 
**exact video and timestamp** where the answer is discussed.

---

## 🚀 Features

- 🎬 Converts video files to audio automatically
- 🗣️ Transcribes + translates audio to English using Whisper
- 🔢 Generates semantic vector embeddings for each text chunk
- 🔍 Finds the most relevant chunks using cosine similarity
- 🤖 Generates a natural language answer with video + timestamp guidance
- 📴 Runs fully offline via Ollama (no API keys needed)

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| Speech-to-Text | OpenAI Whisper (large-v2) |
| Embeddings | bge-m3 via Ollama |
| LLM | LLaMA 3.2 via Ollama |
| Vector Search | Cosine Similarity (scikit-learn) |
| Data Storage | Pandas + joblib |

---

## 📁 Project Structure

```
├── videos/              # Place your input video files here
├── audios/              # Auto-generated MP3 files
├── jsons/               # Auto-generated transcription chunks
├── embeddings.joblib    # Saved vector embeddings
├── process_video.py     # Step 1: Video → MP3
├── stt.py               # Step 2: MP3 → JSON chunks (single file)
├── create_chunks.py     # Step 2: MP3 → JSON chunks (batch)
├── read_chunks.py       # Step 3: JSON → Embeddings
└── process_incoming.py  # Step 4: Query → Answer
```

---

## ⚙️ Setup

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai) installed and running
- ffmpeg installed

### Install dependencies
```bash
pip install openai-whisper pandas scikit-learn joblib requests
```

### Pull required Ollama models
```bash
ollama pull bge-m3
ollama pull llama3.2
```

---

## ▶️ How to Run

**Step 1 — Add videos** to the `videos/` folder

**Step 2 — Convert to MP3**
```bash
python process_video.py
```

**Step 3 — Transcribe to JSON chunks**
```bash
python create_chunks.py
```

**Step 4 — Generate embeddings**
```bash
python read_chunks.py
```

**Step 5 — Ask questions!**
```bash
python process_incoming.py
```

---

## 💡 Example

```
Ask a question: Why couldn't people register?

→ The answer can be found in video "recording4" around timestamp 3.48s - 7.96s.
  The stadium had a capacity of only 60,000 but more than 1 lakh people 
  wanted to register.
```

---

## 📌 Notes

- Whisper's `task="translate"` means videos in **any language** are 
  automatically translated to English
- All processing happens locally — your data never leaves your machine
```
