from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField( upload_to = 'profiles/', null=True)
    user_bio = HTMLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
     
    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save() 

    def get_absolute_url(self): 
        return reverse('user_profile')  

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile  

      

class Image(models.Model):
    image = models.ImageField(default='default.jpg', upload_to = 'images/', blank = True)
    caption = HTMLField()
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
    poster = models.ForeignKey(User, related_name = "images", blank = True)
    pub_date = models.DateTimeField(auto_now = True, blank = True)
  

    @classmethod
    def get_image(cls):

       return cls.objects.all()

    def total_likes(self):
       return self.likes.count

    def search_by_user(cls, search_term):
        images = cls.objects.filter(image_caption__icontains=search_term)
        return images  

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile    

    @classmethod
    def get_profile_images(cls, poster):
        images = Image.objects.filter(poster__pk = poster)
        return images


    @classmethod
    def get_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image   

    def save_image(self):
        self.save()

    def delete_image(self):
        cls.objects.get(id = self.id).delete()

    def update_caption(self):
        self.caption = new_caption
        self.save()

    def update_image(self,val):
       
       Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def get_absolute_url(self): 
        return reverse('index')   

    @classmethod
    def get_photos(cls):
       return cls.objects.all()
    
    
     
    

class Comments(models.Model):
    comment = models.CharField(max_length = 100, blank = True)
    image = models.ForeignKey(Image, related_name = "comments")
    user = models.ForeignKey(User, related_name = "comments")

    def save_comment(self):
        self.save()
    
    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments