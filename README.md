# 🎙️ Niaa Voice Translator 🌐  
_Your personal multilingual voice assistant — powered by AI, voice recognition, and Murf TTS._

![Niaa Demo](https://img.shields.io/badge/Voice%20AI-Niaa-blueviolet?style=for-the-badge&logo=python)  
![Tech Stack](https://img.shields.io/badge/Stack-Flask%20%7C%20Murf%20API%20%7C%20JavaScript%20%7C%20HTML%2FCSS-informational?style=for-the-badge)

## 🧠 What is Niaa?

**Niaa** is a smart, browser-based voice assistant that captures your speech, translates or processes it using AI, and responds back using natural-sounding Murf API voices. Think of it as a voice-powered AI translator and responder — packaged with a clean, futuristic UI.

### 🔑 Features
- 🎤 **Voice input via browser microphone**
- 🗣️ **Speech synthesis using Murf API**
- 🌐 **Multilingual translation-ready**
- ⚡ **Responsive neon-themed UI**
- 🧠 **AI processing hook-ready** (e.g., integrate Gemini/GPT for intelligent replies)

---

## 🚀 Live Demo

> 🔗 Coming Soon (Vercel/Render deployment planned)

---

## 🛠️ Tech Stack

| Frontend        | Backend       | AI + Audio |
|----------------|---------------|------------|
| HTML / CSS     | Flask (Python) | Murf TTS API |
| JavaScript     | REST API       | (Optional) Gemini / GPT for AI |

---

## 📂 Project Structure

niaa-voice-translator/
├── static/
│ ├── css/
│ └── js/
├── templates/
│ └── index.html
├── app.py
├── murf.py # Handles Murf API interactions
├── requirements.txt
└── README.md



---

## 🧪 How It Works

1. User clicks the mic button 🔴 and speaks.
2. Voice is captured using `Web Speech API`.
3. Text is sent to Flask backend → (Optional AI processing).
4. Flask calls Murf API to synthesize the response.
5. Audio is streamed back and played in-browser.

---

## 🔧 Setup & Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/earlywinter96/niaa-voice-translator.git
cd niaa-voice-translator

pip install -r requirements.txt

In murf.py:

api_key = "your-murf-api-key"

python app.py


🎯 Roadmap
 Mic Input via Browser

 Murf TTS Response Playback

 Language toggle / Translation feature

 Gemini AI integration

 Deploy to Vercel / Render

 Wake word: "Hey Niaa"

🖼️ UI Preview
(Add screenshots or Loom demo link here)

📬 Feedback & Contributions
Got ideas? Found a bug?
Open an Issue or submit a Pull Request.

📄 License
MIT License. See LICENSE file for details.

Built with ❤️ by EarlyWinter96

yaml
Copy
Edit

---

Would you like me to include:
- A custom logo for Niaa?
- Screenshot placeholders or UI GIF preview?
- Deployment instructions for Render/Vercel?

Let me know and I’ll add them!
