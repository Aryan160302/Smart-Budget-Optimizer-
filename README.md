# Smart-Budget-Optimizer-



A Django-based Financial Decision Support Dashboard for managing EMIs, personal budgets, and AI-driven financial recommendations.  

It allows users to:
- 📌 Manage loans and EMI schedules  
- 📌 Track monthly expenses and remaining budget  
- 📌 Get real-time AI-generated financial tips using **open-source local LLMs (Ollama + LLaMA 2)**  
- 📊 Visualize financial summaries and decision support in one place

---

## 📦 Features

- 🔐 User Authentication (Sign-up / Login)
- 📄 EMI Management: Add, view, and delete EMI records
- 📈 Budget Optimizer: Track expenses, remaining money, and remove entries
- 🤖 AI-Powered Recommendations via **Ollama (local LLaMA 2 model)**
- 💡 Smart financial suggestions based on user queries and real data
- Clean, responsive front-end with Bootstrap

---

## 📂 Project Structure

```
finance_dashboard/
├── finance_dashboard/        # Main project settings
│   └── ...
├── finance_app/              # Core app with views, models, templates
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
├── templates/
│   └── base.html
├── manage.py
└── requirements.txt
```

---

## 🛠️ Installation & Setup  

### 1️⃣ Install Python dependencies:
```bash
pip install -r requirements.txt
```

### 2️⃣ Install and setup Ollama (local AI server)
> Ollama runs local LLMs like LLaMA 2 without any cloud API usage

**Install Homebrew (if missing):**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Install Ollama:**
```bash
brew install ollama
```

**Start the Ollama server:**
```bash
ollama serve
```

**Pull the LLaMA 2 model:**
```bash
ollama pull llama2
```

---

## 📊 Running the Project  

**Start the Django server:**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

**Important:** Make sure **`ollama serve`** is running in a separate terminal window.

---

## ⚙️ AI Recommendations API  

**Endpoint:**  
`POST /get_recommendations/`

**Request Body:**
- `prompt` (string)

**Response:**
- AI-generated financial advice based on the prompt

Example:
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Best money-saving tips for students"
}'
```

---

## 📊 Future Improvements (Optional)

- 📈 Add data visualization with Chart.js / Recharts
- 📤 CSV export for EMI and expense reports
- 📱 Progressive Web App (PWA) support
- 🌐 Host on Vercel / Render / Railway
- 🛡️ Add CSRF protection in production

---

## 📸 Screenshots  

> (Add screenshots of your dashboard UI and AI tips section here if possible)

---

## 📝 License  

MIT License  

---

## ✨ Credits  

Built with ❤️ by Aryan Chaturvedi  
Open-source LLM backend: [Ollama](https://ollama.ai/)  
Model: Meta's LLaMA 2

---
