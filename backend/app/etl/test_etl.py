from app.etl.scraper import scrape_courses
from app.etl.transformer import transform_eligibility
from app.etl.loader import load_data

raw = scrape_courses()
structured = transform_eligibility(raw)
load_data(raw, structured)

print("ETL completed successfully")
