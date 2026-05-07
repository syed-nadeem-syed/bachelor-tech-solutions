from django.urls import path
from . import views

urlpatterns = [

    # Home Page
    path('', views.home, name='home'),

    # Services Page
    path('services/', views.services, name='services'),

    # Projects Page
    path('projects/', views.projects, name='projects'),

    # About Page
    path('about/', views.about, name='about'),

    # Contact Page
    path('contact/', views.contact, name='contact'),

]