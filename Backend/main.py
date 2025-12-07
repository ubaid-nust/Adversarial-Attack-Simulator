from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app_fgsm import app as fgsm_app

# Create main FastAPI app
app = FastAPI(title="Adversarial Attack API")

# Mount FGSM app at root
app.mount("/", fgsm_app)

# Enable CORS for your Amplify frontend
origins = ["https://main.d379q9b3vj57kv.amplifyapp.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)