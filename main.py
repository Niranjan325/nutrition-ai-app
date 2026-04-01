from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Backend running 🚀",
        "app_name": os.getenv("APP_NAME")
    }

@app.get("/health")
def health():
    return {"status": "OK"}