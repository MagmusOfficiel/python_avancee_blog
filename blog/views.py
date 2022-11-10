from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "blog/index.html")

def blog(request, numero_blog):
    if numero_blog in ["01", "02", "03"]:
        return render(request, f"blog/blog_{numero_blog}.html", context={})
    return render(request, "blog/blog_not_found.html")