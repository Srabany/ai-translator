from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
import pycountry
import os

app = Flask(__name__)

# Get dictionary {Full Name: Code}
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

@app.route("/languages", methods=["GET"])
def languages():
    return jsonify(get_languages())

@app.route("/translate", methods=["POST"])
def translate_api():
    data = request.json
    original_text = data.get("text", "")
    input_lang = data.get("input_lang", "en")
    target_lang = data.get("target_lang", "bn")

    if not original_text.strip():
        return jsonify({"error": "No text provided"}), 400

    try:
        translated_text = GoogleTranslator(
            source=input_lang, target=target_lang
        ).translate(original_text)
        return jsonify({
            "original_text": original_text,
            "translated_text": translated_text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
