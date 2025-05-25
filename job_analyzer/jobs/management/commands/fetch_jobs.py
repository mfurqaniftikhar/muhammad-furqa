from django.core.management.base import BaseCommand
from jobs.scraper.indeed_scraper import scrape_indeed
# from jobs.scraper.rozee_scraper import scrape_rozee  # if available

class Command(BaseCommand):
    help = 'Fetches jobs from Indeed and Rozee'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Scraping Indeed...'))
        scrape_indeed("python developer")  # Query jo aap chahen
        self.stdout.write(self.style.SUCCESS('Scraping Rozee...'))
        # scrape_rozee("python developer")
        self.stdout.write(self.style.SUCCESS('All jobs scraped!'))