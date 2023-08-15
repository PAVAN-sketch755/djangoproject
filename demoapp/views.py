from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def home (request):
    post=Blog.objects.all()
    
    return render(request, "base.html",{'post':post})
