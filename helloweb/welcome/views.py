from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
        Hello World. Welcome to Yingbo (Max) Wang's personal website.
        Powered by Django.
    """)
