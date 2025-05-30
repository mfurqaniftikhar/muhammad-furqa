import json
from django.shortcuts import render

def dashboard(request):
    # Example data (replace with your querysets)
    job_titles = {'Python Developer': 10, 'Data Scientist': 7, 'Frontend Dev': 5,'Backend':11}
    skills = {'java':15,'Python': 12, 'Django': 9, 'React': 6}
    cities = {'Lahore': 7, 'Karachi': 6, 'Islamabad': 4}
    sources = {'Indeed': 9, 'Glassdoor': 8}

    context = {
        'job_titles': json.dumps(job_titles),
        'skills': json.dumps(skills),
        'cities': json.dumps(cities),
        'sources': json.dumps(sources),
    }
    return render(request, "jobs/dashboard.html", context)