# AI Voice Assistant Agent (Gen AI Chatbot)

A locally-run voice-enabled AI assistant built with the Mistral model via Ollama, using Vosk for offline speech recognition, pyttsx3 for text-to-speech, and SQLite for memory. The assistant runs through a clean and minimal Streamlit web UI.

---

## 🔧 Tech Stack

🧠 LLM: Mistral via Ollama

🎙️ Voice Input: Vosk

🗣️ Voice Output: pyttsx3

💾 Memory: SQLite

🖥️ UI: Streamlit

📝 Language: Python 3.10+

---

## 🚀 Features

🔊 Offline voice interaction: listens to your speech and replies by voice

🧠 Local inference with Mistral via Ollama (no internet required after setup)

💬 Context-aware assistant with persistent memory (SQLite)

🌐 Lightweight Streamlit UI for input/output tracking

---

## 🧠 Memory (SQLite Schema)

```sql

CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    response TEXT,
    status TEXT NOT NULL,         -- 'success', 'error', 'timeout'
    response_time_ms INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## ▶️ How to Run

1. Start Ollama Server (Terminal 1)
   
```bash
ollama serve
```

2. Pull and Run the Mistral Model (Terminal 2)
```bash
ollama run mistral
```
⚠️ Leave both terminals running.

3. Run the Streamlit App (Terminal 3)
```bash
streamlit run main.py
```

---


## 🔊 Voice Input (Vosk)

Download vosk-model-small-en-us-0.15

Place the model folder in the project root

assistant.py will load the model automatically at runtime

---

## 🗣️ Voice Output (pyttsx3)

Uses your system’s TTS engine

Works offline and cross-platform (Windows/macOS/Linux)

---

## 📌 Use Cases
Personal AI assistant (offline-friendly)

Education or productivity companion

Local GenAI prototype for voice applications

---

## 📸 Screenshots

