from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home,name='home'),    
    url(r'^profile', views.profile, name = 'profile'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
    url(r'^likes/$', views.like_image, name='like_image'),
    url(r'^image/(\d+)', views.image, name = 'image'),
    url(r'^search/', views.search_results, name='search_results'),  
]   

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)