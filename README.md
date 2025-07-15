# 🏋️ HomeFit - Gerador de Planos de Treino em Casa  

Micro SaaS que gera planos de treino personalizados via e-mail.  

## 🛠️ Tecnologias  
- **Back-end**: FastAPI (Python)  
- **Front-end**: Vue.js (HTML/CSS/JS)  
- **Deploy**: Render.com (API) + Vercel (Front-end)  

## ⚡ Como Executar Localmente  

### Back-End (FastAPI)  
```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn main:app --reload