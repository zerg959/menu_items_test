from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('team', views.about, name='team'),
    path('page3', views.about, name='page3'),
    path('about/contacts', views.about, name='contacts'),
    path('admin/', admin.site.urls),
]
