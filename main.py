from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from database import users_collection

load_dotenv()

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

@app.get("/")
def home():
    return {
        "message": "Backend running 🚀",
        "app_name": os.getenv("APP_NAME")
    }

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/signup")
def signup(user: UserCreate):

    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    result = users_collection.insert_one({
        "name": user.name,
        "email": user.email,
        "password": user.password  # plain text (as requested)
    })

    return {
        "message": "User created successfully",
        "user_id": str(result.inserted_id)
    }
