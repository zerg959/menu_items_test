from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('page3', views.page3, name='page3'),
    path('about/contacts', views.contacts, name='contacts'),
    path('admin/', admin.site.urls),
    path('projects/', views.projects, name='projects'),
    path('projects/project1', views.project1, name='project1'),
]
