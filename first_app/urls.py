"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='INDEX'),
    path('about_us/',views.about_us,name='About Us'),
    path('upload',views.upload,name='upload'),
    path('contact/',views.contact,name='Contact'),
    path('feedback/',views.feedback,name='Feedback'),
    path('bugs/',views.bugs,name='Report Bugs'),
    path('home/',views.home,name='Mane'),
    path('profile/',views.profile,name='Profile'),
    path('friends/',views.friends,name='Friends'),
    path('chat/',views.chat,name='Chat'),
    path('signup',views.handleSignup,name='Sign Up'),
    path('login',views.handleLogin,name='Log In'),
    path('logout',views.handleLogout,name='Log Out'),
    path('profilecreated/',views.profilecreated,name='Your Profile Is Created'),
    path('login/',views.login,name='LOG IN'),
    path('signup',views.signup,name='SIGN UP'),
    


]
