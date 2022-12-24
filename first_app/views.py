from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Post
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'profile\signup.html')
    
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
     return render(request,'contact.html')

def about_us(request):
    return render(request,'about_us.html')

def feedback(request):
    return render(request,'feedback.html')

def bugs(request):
    return render(request,'bugs.html')

@login_required(login_url='/login')
def profile(request):
    return render(request,'profile.html')

def friends(request):
    return render(request,'friends.html')

def chat(request):
    return render(request,'chat.html')

def profilecreated(request):
    return render(request, 'profilecreated.html')


def handleSignup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        #check for bad inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/home')

        if not username.isalnum():
            messages.error(request, "Username should only contain alphabets and numbers")
            return redirect('/home')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Already Taken')
            return redirect('/signup')

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Taken')
            return redirect('/signup')


        #create the user
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()
        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        messages.info(request, "Your account have been created")
        return redirect('/home')

    else:
        return redirect('/home')


def handleLogin(request):
     if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = auth.authenticate(username=loginusername,
        password=loginpassword)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
            # login(request, user)
            # messages.info(request, "Successfully Logged In")
            # return redirect('/profile')
        else:
            messages.info(request, 'Invalid Details!')
            return redirect('/login')
            # messages.error(request, "Invalid Details, Please Log In Again")          
            # return redirect('/home')

        return redirect('/home')

def handleLogout(request):
    auth.logout(request)
    messages.info(request, "Successfully logged out")
    return redirect('/home')


@login_required(login_url='/login')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

    else:
        return redirect('/')

# def about(request):
#     return render(request,'home/about.html')