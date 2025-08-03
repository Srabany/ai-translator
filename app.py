from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
import pycountry
import os

app = Flask(__name__)

# Function to get dictionary {Full Name: Code}
def get_languages():
    langs = GoogleTranslator().get_supported_languages(as_dict=True)
    full_names = {}
    for code, name in langs.items():
        try:
            lang_full = pycountry.languages.get(alpha_2=code)
            if lang_full:
                full_names[lang_full.name] = code
            else:
                full_names[name.capitalize()] = code
        except:
            full_names[name.capitalize()] = code
    return dict(sorted(full_names.items()))

# API route for languages
@app.route("/languages", methods=["GET"])
def languages_api():
    return jsonify(get_languages())

# API route for translation
@app.route("/translate", methods=["POST"])
def translate_api():
    data = request.get_json()
    text = data.get("text", "")
    input_lang = data.get("input_lang", "auto")
    target_lang = data.get("target_lang", "en")

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    try:
        translated_text = GoogleTranslator(source=input_lang, target=target_lang).translate(text)
        return jsonify({
            "original_text": text,
            "translated_text": translated_text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
