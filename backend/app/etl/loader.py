from app.database.mongo import courses_collection, eligibility_collection

def load_data(course_data: dict, eligibility_data: dict):
    course_result = courses_collection.insert_one({
        "university": course_data["university"],
        "course_name": course_data["course_name"],
        "field": "IT",
        "level": "Degree"
    })

    eligibility_collection.insert_one({
        "course_id": course_result.inserted_id,
        **eligibility_data
    })
