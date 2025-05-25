import requests
from bs4 import BeautifulSoup
from jobs.models import Job
import time

def scrape_rozee(keyword="software", location="Pakistan", max_pages=1):
    for page in range(1, max_pages + 1):
        url = f"https://www.rozee.pk/job/jsearch/q/{keyword}/l/{location}/pn/{page}"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        for card in soup.select('div.job_list'):
            title = card.select_one('a.job_title')
            company = card.select_one('span.company_name')
            loc = card.select_one('span.location')
            date_posted = card.select_one('span.date')
            skills = card.select_one('div.skill_set')
            Job.objects.create(
                source="Rozee",
                title=title.text.strip() if title else "",
                company=company.text.strip() if company else "",
                location=loc.text.strip() if loc else "",
                skills=skills.text.strip() if skills else "",
                date_posted=date_posted.text.strip() if date_posted else ""
            )
        time.sleep(1)