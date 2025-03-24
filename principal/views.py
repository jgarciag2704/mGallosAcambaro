from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    title = "Predicción de verduras"
    return render(request, "index.html", {'title': title})


