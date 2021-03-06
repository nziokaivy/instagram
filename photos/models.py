from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse


# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField( upload_to = 'profiles/', null=True)
    user_bio = models.CharField(max_length = 100, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
     
    
    def save_profile(self):
        self.save() 

    def get_absolute_url(self): 
        return reverse('user_profile')  

     

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile    

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile 
    
    def __str__(self):
        return f'{self.user.username} Profile'


class Image(models.Model):
    image = models.ImageField( upload_to = 'images/', blank = True)
    caption = models.CharField(max_length = 100, blank = True)
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
    poster = models.ForeignKey(User, related_name = "images", blank = True)
    pub_date = models.DateTimeField(auto_now = True, blank = True)
    


    def total_likes(self):
       return self.likes.count

    def search_by_user(cls, users):
        images = cls.objects.filter(image_caption__icontains=users)
        return cls.objects.filter(user_id = user.id) 

      

    @classmethod
    def get_profile_images(cls, poster):
        images = Image.objects.filter(poster__pk = poster)
        return images


    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.get(id = self.id).delete()


    def update_caption(self):
        self.caption = new_caption
        self.save()


    @classmethod
    def get_absolute_url(self): 
        return reverse('home')   

    @classmethod
    def get_photos(cls):
       return cls.objects.all()

    def __str__(self):
        return self.image       
    
class Comments(models.Model):
    comment = models.CharField(max_length = 100, blank = True)
    image = models.ForeignKey(Image, related_name = "comments")
    author = models.ForeignKey(User, related_name = "author")
    pub_date = models.DateTimeField(auto_now_add = True,null = True)
    


    def save_comment(self):
        self.save()
    
    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments

    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()    

    def __str__(self):
        return self.comment    