import requests
from bs4 import BeautifulSoup

def extract_text(data, t):
    if t == "Job Description URL":
        html = requests.get(data).text
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()
    return data
