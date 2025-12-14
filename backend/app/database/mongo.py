from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "ai_course_eligibility"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

# Collections
students_collection = db["students"]
courses_collection = db["courses"]
eligibility_collection = db["eligibility_rules"]
logs_collection = db["logs"]
