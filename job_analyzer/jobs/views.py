# jobs/views.py

from django.shortcuts import render
from .models import Job

def dashboard(request):
    jobs = Job.objects.all().order_by('-date_posted')[:200]
    return render(request, "jobs/dashboard.html", {"jobs": jobs})