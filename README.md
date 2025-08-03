# 🌍 Smart AI Translator - Backend

This is the **backend** for Smart AI Translator, built with **Flask** and powered by the **Google Translate API** via `deep-translator`.  
It provides API endpoints to fetch supported languages and translate text.  
The backend is designed to work with the frontend hosted separately (e.g., Vercel).

---

## 📂 Project Structure

ai-translator/
│── app.py # Main Flask backend API
│── requirements.txt # Python dependencies
│── Procfile # For Render deployment
│── runtime.txt # Python version for deployment
│── .gitignore # Ignore venv, cache, etc.
│── README.md # Project documentation
│── venv/ # Virtual environment (not pushed to GitHub)


---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/YOUR-USERNAME/ai-translator.git
cd ai-translator

### 2️⃣ Create a Virtual Environment & Activate

python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # Mac/Linux

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Run Locally

python app.py

Visit: http://127.0.0.1:5000

## 🌐 API Endpoints
1. Get Supported Languages
GET /languages

curl http://127.0.0.1:5000/languages

2. Translate Text
POST /translate

curl -X POST http://127.0.0.1:5000/translate \
-H "Content-Type: application/json" \
-d '{"text": "Hello", "input_lang": "en", "target_lang": "fr"}'

## 🚀 Live Demo
🌐 Try it here: https://translator-frontend-ldjz.vercel.app/

## 🔄 Related Repositories

Frontend Repository (HTML + JS on Vercel) → https://github.com/Srabany/translator-frontend

## 📌 Note:
You can visit the frontend repo to check the UI.

