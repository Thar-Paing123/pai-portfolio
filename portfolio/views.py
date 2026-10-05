from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from .data import EDUCATION, EXPERIENCE, PROJECTS, SKILLS


def home(request):
    return render(request, 'portfolio/home.html', {'skills': SKILLS, 'experience': EXPERIENCE, 'projects': PROJECTS, 'education': EDUCATION})


def resume(request):
    return FileResponse(open(settings.BASE_DIR / 'portfolio/static/portfolio/assets/resume.pdf', 'rb'), as_attachment=True, filename='Phyo_Thet_Paing_Resume.pdf', content_type='application/pdf')
