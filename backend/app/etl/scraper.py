import requests
from bs4 import BeautifulSoup

def scrape_courses():
    """
    Scrapes course and eligibility text from a university website.
    (Example structure – adaptable per university)
    """
    url = "https://www.nsbm.ac.lk/course/bsc-in-it/"  # example
    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "university": "NSBM",
        "course_name": "BSc in IT",
        "raw_eligibility": ""
    }

    eligibility_section = soup.find("div", class_="entry-content")
    if eligibility_section:
        data["raw_eligibility"] = eligibility_section.get_text(strip=True)

    return data
