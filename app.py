from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
import pycountry
import os
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  

@app.route("/languages", methods=["GET"])
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
    return jsonify(dict(sorted(full_names.items())))


@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text", "")
    input_lang = data.get("input_lang", "en")
    target_lang = data.get("target_lang", "en")
    translated = GoogleTranslator(source=input_lang, target=target_lang).translate(text)
    return jsonify({
        "original_text": text,
        "translated_text": translated
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
