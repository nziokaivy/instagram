from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image, Profile, Comments
from django.contrib.auth.decorators import login_required
# Create your views here.



def home(request):
    current_user = request.user
    images = Image.objects.order_by('-pub_date') 
    profile = Profile.objects.order_by('_last_update')  
    return render(request,'index.html', {'images':images})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user 
    images = Image.objects.order_by('-pub_date')      
    return render(request, 'profile.html', {"user":user, "current_user":request.user, "images":images})    

