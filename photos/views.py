from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image, Profile, Comments,User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import  CommentForm, ImageForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    images = Image.objects.order_by('-pub_date')
    profiles = Profile.objects.order_by('-last_update')
    
    return render(request, 'index.html', {'images':images, 'profiles':profiles})

@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user = request.user
    user = current_user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.poster = user
            image.save()
            return redirect('home')
    else:
        form = ImageForm()
    
    return render(request, 'upload_image.html', {'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user    
    images = Image.objects.all().filter(poster_id = user.id)
    return render(request, 'profile.html', {'images':images, "user":user, "current_user":request.user })
    
@login_required(login_url='/accounts/login/')
def image(request,image_id):

    image = Image.get_image_id(id = image_id)
    comments = Comments.get_comments_by_images(image_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.author = request.user.username
            comment.save()
        return redirect('home')

    else:
        form = CommentForm()

    is_liked = False
    if image.likes.filter(id = request.user.id).exists():
        is_liked = True    

   
    return render(request,"image.html", {"image":image,"is_liked":is_liked,"total_likes":image.total_likes(),'comments':comments,'form':form})

@login_required(login_url='/accounts/login/')
def like_image(request):
    images = get_object_or_404(Image,id = request.POST.get('image_id') )
    is_liked = False
    if images.likes.filter(id = request.user.id).exists():
        images.likes.remove(request.user)
        is_liked = False
    else:
        images.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect(images.get_absolute_url())

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})