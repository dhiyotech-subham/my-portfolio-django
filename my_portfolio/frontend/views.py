from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(req):
    context = {
        'name': "Subham Barman",
        'age': 2,
        'fruits': ['apple', 'mango', 'banana', 'orange']
    }
    return render(req, "sample.html", context)
def home(req):
    return render(req, "pages/index.html")
def about(req):
        return render(req, "pages/about.html")
def contact(req):
        return render(req, "pages/contact.html")
def blogs(req):
        return render(req, "pages/blogs.html")
def services(req):
        return render(req, "pages/services.html")
def projects(req):
        return render(req, "pages/projects.html")