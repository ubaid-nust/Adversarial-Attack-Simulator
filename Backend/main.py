from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app_fgsm import app as fgsm_app

app = FastAPI(
    title="FGSM Attack API",
    description="Backend for adversarial attack simulation",
    version="1.0.0"
)

# CORS
origins = [
    "https://main.d379q9b3vj57kv.amplifyapp.com",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👉 MERGE ROUTES, DO NOT MOUNT
app.include_router(fgsm_app.router, prefix="/attack")