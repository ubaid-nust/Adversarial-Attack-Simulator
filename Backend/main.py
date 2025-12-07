# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app
app = FastAPI(title="Adversarial Attack API")

# CORS setup for your frontend
origins = ["https://main.d379q9b3vj57kv.amplifyapp.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy /attack endpoint
# Replace the body with your actual FGSM attack logic
@app.post("/attack/")
async def attack(file: UploadFile = File(...)):
    contents = await file.read()
    # Your FGSM attack code here using `contents`
    return {"filename": file.filename, "message": "Attack executed successfully!"}