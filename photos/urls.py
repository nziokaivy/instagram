from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home,name='home'),    
    url(r'^accounts/profile/', views.profile, name = 'profile'),
    url(r'^likes/$', views.like_image, name='like_image'),
    url(r'^image/(?P<image_id>\d+)', views.image, name='image'),
    url(r'^search/', views.search, name='search'),  
]   

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)