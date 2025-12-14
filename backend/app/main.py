from fastapi import FastAPI
from app.database.mongo import db

app = FastAPI(title="AI Course Eligibility System")

@app.get("/")
def root():
    return {
        "message": "API running",
        "database": db.name
    }
