from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def root_page(request):
    return HttpResponse("<h1>OK MEC</h1>")
