from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, "home.html")

def about (request):
    return render (request, "about.html")

def projects(request):
    projects_show = [
        {
            "title": "SmartOSM",
            "path": "images/smartOSM.png"
        },
        {
            "title": "Pro-digi",
            "path": "images/prodigi.png"
        }
    ]
    return render (request, "projects.html",  {"projects_show": projects_show})