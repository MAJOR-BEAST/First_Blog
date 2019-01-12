from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainblog-index'),
    path('about/', views.about, name='mainblog-about'),
    path('Services/', views.Services, name='mainblog-Services')
    
]