from fastapi import FastAPI
from app.database.mongo import db
from app.api import admin

app = FastAPI(title="AI Course Eligibility System")

# Register admin routes
app.include_router(admin.router)

@app.get("/")
def root():
    return {
        "message": "API running",
        "database": db.name
    }
