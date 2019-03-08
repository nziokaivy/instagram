from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image, Profile, Comments
# Create your views here.


def home(request):
  
    return render(request, 'index.html')

