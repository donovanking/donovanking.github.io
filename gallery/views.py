from django.shortcuts import render
from .models import Image

def index(request):
    return render(request, 'index.html', {})

def info(request):
    return render(request, 'info.html', {})

def gallery_view(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'gallery/gallery_view.html', context)