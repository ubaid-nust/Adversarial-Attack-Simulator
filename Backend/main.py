from fastapi.middleware.cors import CORSMiddleware
from app.app_fgsm import app

# Only allow your deployed frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://main.d379q9b3vj57kv.amplifyapp.com"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app_fgsm:app", host="0.0.0.0", port=8000, reload=True)