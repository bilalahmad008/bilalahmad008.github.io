from django.shortcuts import render

from django.http.response import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "console/index.html")

