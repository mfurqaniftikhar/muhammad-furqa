from django.db import models

class Job(models.Model):
    scraped_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    date_posted = models.DateField()
    source = models.CharField(max_length=255)
    scraped_at = models.DateTimeField(auto_now_add=True)  # <-- Yeh line yahan add karein!

    def __str__(self):
        return self.title