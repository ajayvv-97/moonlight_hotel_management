from django.urls import path,include
from . import views
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
    path('account_creation',views.account_creation,name='account_creation'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
