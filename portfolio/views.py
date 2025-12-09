# ============================================
# portfolio/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Project
from django.http import JsonResponse
import json

def index(request):
    projects = Project.objects.all()[:6]
    # Prepare a list of technologies for each project so templates can iterate safely
    for p in projects:
        if p.technologies:
            p.tech_list = [t.strip() for t in p.technologies.split(',') if t.strip()]
        else:
            p.tech_list = []
    return render(request, 'portfolio/index.html', {'projects': projects})

def contact_submit(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            contact = Contact.objects.create(
                name=data['name'],
                email=data['email'],
                subject=data['subject'],
                message=data['message']
            )
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

