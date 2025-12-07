# FGSM Adversarial Attack — Image Classification (Animals)

This project demonstrates how adversarial attacks can fool a trained deep learning model using the **Fast Gradient Sign Method (FGSM)**.  
Users can upload an image, view the clean prediction, generate an adversarial version, and observe how a tiny perturbation can change the model’s output.

---

## How to Run Locally

1️⃣ Backend (FastAPI + PyTorch)

#### Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

#### Start the backend server

cd backend
python main.py

2️⃣ Frontend (Next.js)

## Install dependencies:
npm install

# Start development server:

npm run dev


# Frontend URL:

http://localhost:3000