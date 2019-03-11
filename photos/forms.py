from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Comments, Image

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment',)

from django import forms

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        exclude=['likes','poster']