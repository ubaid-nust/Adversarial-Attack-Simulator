from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app_fgsm import app as fastapi_app

# Create FastAPI application
app = FastAPI()

# Mount your existing app inside this main app
app.mount("/", fastapi_app)

# CORS for your Amplify frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://main.d379q9b3vj57kv.amplifyapp.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
