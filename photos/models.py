from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField( upload_to = 'profiles/', null=True)
    user_bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
     
    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save() 

      

class Image(models.Model):
    image = models.ImageField(default='deafault.jpg', upload_to = 'images/', blank = True)
    caption = models.CharField(max_length = 50, blank = True)
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
    poster = models.ForeignKey(User, related_name = "posts", blank = True)
    pub_date = models.DateTimeField(auto_now_add = True, blank = True)
  

    @classmethod
    def get_image(cls):

       return cls.objects.all()

    def save_image(self):
        self.save()

    def delete_image(self):
        cls.objects.get(id = self.id).delete()

    def update_caption(self):
        self.caption = new_caption
        self.save()

class Comments(models.Model):
    comment = models.CharField(max_length = 100, blank = True)
    image = models.ForeignKey(Image, related_name = "comments")
    user = models.ForeignKey(User, related_name = "comments")