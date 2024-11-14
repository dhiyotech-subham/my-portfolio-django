from django.urls import path
from . import views

urlpatterns = [
    path('/sample', views.sample, name="sample"),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('blogs/', views.blogs, name="blogs"),
    path('services/', views.services, name="services"),
    path('projects/', views.projects, name="projects"),
]   