from django.shortcuts import render


# Home Page
def home(request):
    return render(request, 'index.html')


# Services Page
def services(request):
    return render(request, 'services.html')


# Projects Page
def projects(request):
    return render(request, 'projects.html')


# About Page
def about(request):
    return render(request, 'about.html')


# Contact Page
def contact(request):
    return render(request, 'contact.html')