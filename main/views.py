from django.shortcuts import render
from .models import Newsletter

# Create your views here.
def home(response):
    news = ""
    if response.method == "POST":
        print(response.method)
        if response.POST.get("button"):
            anold = Newsletter(subscription=response.POST.get("email"), name = "anold" )
            anold.save()
            news = "thanks for being part of us!"


    return render(response,'main/home.html',{"news":news})