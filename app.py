from flask import Flask, request, jsonify, render_template, send_from_directory
from murf import Murf
from translatepy import Translator
import os

app = Flask(__name__)
MURF_API_KEY = "ap2_5500839b-f2dd-407a-bcba-9025e40a70ff"  # Replace this
client = Murf(api_key=MURF_API_KEY)
translator = Translator()

# Fallback voice list if fetching from API fails
FALLBACK_VOICES = [
    {"id": "en-IN-amala", "name": "Amala (Indian Female)"},
    {"id": "en-US-natalie", "name": "Natalie (US Female)"},
    {"id": "en-GB-harry", "name": "Harry (UK Male)"}
]

@app.route("/")
def index():
    voices = FALLBACK_VOICES
    return render_template("index.html", voices=voices)

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")
    selected_voice = data.get("voice", "")
    target_lang = data.get("language", "en")

    if not text or not selected_voice:
        return jsonify({"error": "Missing text or voice"}), 400

    try:
        print(f"🗣 Received text: {text}")
        print(f"🌐 Target lang: {target_lang}")
        print(f"🧬 Voice ID: {selected_voice}")

        # Translate to English if needed
        if target_lang != "en":
            translated = translator.translate(text, "en").result
        else:
            translated = text

        print(f"🔁 Translated text: {translated}")

        # Murf API call
        result = client.text_to_speech.generate(
            format="MP3",
            sample_rate=44100.0,
            text=translated,
            voice_id=selected_voice
        )

        print("✅ Murf API result:", result)

        if hasattr(result, "audio_file") and result.audio_file:
            return jsonify({
                "original": text,
                "translated": translated,
                "audio": result.audio_file
            })

        return jsonify({"error": "No audio returned from Murf"}), 500

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('images', filename)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
