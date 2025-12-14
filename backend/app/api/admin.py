from fastapi import APIRouter
from app.database.mongo import courses_collection, eligibility_collection

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/course")
def add_course(course: dict):
    courses_collection.insert_one(course)
    return {"message": "Course added successfully"}

@router.post("/eligibility")
def add_eligibility(rule: dict):
    eligibility_collection.insert_one(rule)
    return {"message": "Eligibility rule added successfully"}
