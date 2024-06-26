from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('home',views.index, name='index'),
     path('register', views.register, name='register'),
     path('login', views.login, name='login'),
     path('home/create', views.creation, name='creation'),
     path('home/list', views.getCreationPage, name='listhome')
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)