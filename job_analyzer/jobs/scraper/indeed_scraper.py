from jobs.models import Job
import datetime

def scrape_indeed(query):
    # Assume yeh list aap scraping karke bana rahe hain:
    scraped_jobs = [
        {
            "title": "Python Developer",
            "company": "ABC Ltd",
            "location": "Lahore",
            "skills": "Python, Django",
            "date_posted": "2025-05-20"  # YYYY-MM-DD format
        },
        # ... aur bhi jobs
    ]

    for job in scraped_jobs:
        try:
            # Convert string to date object if necessary:
            date_obj = datetime.datetime.strptime(job["date_posted"], "%Y-%m-%d").date()
            Job.objects.create(
                title=job["title"],
                company=job["company"],
                location=job["location"],
                skills=job["skills"],
                date_posted=date_obj,
                source="Indeed"
            )
            print(f"Job saved: {job['title']}")
        except Exception as e:
            print(f"Error saving job: {job['title']}. Reason: {e}")