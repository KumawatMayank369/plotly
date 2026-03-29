# 📈 ML Regression Predictor

A clean web form + FastAPI backend for a Scikit-learn regression model.
Hosted 100% free using **GitHub Pages** + **Hugging Face Spaces**.

---

## 📁 Repo Structure

```
my-ml-app/
├── index.html       ← Web form (deployed via GitHub Pages)
├── main.py          ← FastAPI backend
├── model.pkl        ← Your trained Scikit-learn model
├── requirements.txt ← Python dependencies
└── README.md
```

---

## 🚀 Deployment (Step-by-Step)

### ① Push to GitHub
```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### ② Enable GitHub Pages (for index.html)
1. Go to repo → **Settings** → **Pages**
2. Source: `main` branch, `/ (root)` → Save
3. Live at: `https://YOUR_USERNAME.github.io/YOUR_REPO/`

### ③ Deploy FastAPI → Hugging Face Spaces (Free)
1. Go to huggingface.co/spaces → Create new Space
2. Pick **Docker** SDK
3. Upload: `main.py`, `model.pkl`, `requirements.txt`, and a `Dockerfile`:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

4. API live at: `https://YOUR_USERNAME-ml-api.hf.space`

### ④ Connect Form to API
In `index.html`, update this line:
```js
const API_URL = "https://YOUR_HF_SPACE.hf.space/predict";
```
Then push to GitHub again — done! ✅

---

## 📦 requirements.txt (must include)
```
fastapi
uvicorn
scikit-learn
numpy
pydantic
```
