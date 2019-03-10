from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image, Profile, Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.



def home(request):
    current_user = request.user
    images = Image.objects.order_by('-pub_date') 
    profile = Profile.objects.order_by('_last_update')  
    return render(request,'index.html', {'images':images})


@login_required(login_url='/accounts/login/')
def profile(request):
    
    user = request.user 
    
    images = Image.objects.all().filter(id=user.id)
     
    return render(request, 'profile.html', {'images':images})    

def image(request,image_id):

    images = Image.objects.get(id = image_id)
    comments = Comments.get_comments_by_images(image_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.author = request.user
            comment.save()
        return redirect('home')
    else:
        form = CommentForm()
        is_liked = False
        if image.likes.filter(id = request.user.id).exists():
            is_liked = True

    return render(request,"image.html", {"image":image,"is_liked":is_liked,"total_likes":image.total_likes(),'comments':comments,'form':form})