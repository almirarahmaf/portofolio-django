from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('qualification/', views.qualification, name='qualification'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact, name='contact'),
]