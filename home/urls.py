from django.urls import path,include
from . import views
from .views import account_registartion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('rooms',views.rooms,name='rooms'),
    path('login',views.login,name='login'),
    path('sign',views.sign,name='sign'),
    path('account_registartion',account_registartion,name='account_registartion'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
