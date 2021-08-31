from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/about', views.about, name='about'),
    path('home/contact', views.contact, name='contact'),
    path('home/dashboard', views.dashboard, name='dashboard'),
    path('home/signup', views.user_signup, name='signup'),
    path('home/login', views.user_login, name='login'),
    path('home/logout', views.user_logout, name='logout'),
    path('home/addpost', views.add_post, name='addpost'),
    path('home/updatepost/<int:id>', views.update_post, name='updatepost'),
    path('home/deletepost/<int:id>', views.delete_post, name='deletepost'),
]