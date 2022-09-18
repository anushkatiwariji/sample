from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from . models import *
from .forms import BlogForm


def home(request):
    return render(request, "webapp/index.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['cpassword']
        if(password == password1):
            user = User.objects.create_user(username=email.split("@")[0], email=email, password=password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            return render(request,'webapp/loginpage.html')

        else:
            messages.error(request, "Email or Password Invalid!")

       
        if len(User.objects.filter(email=email)) != 0:
            messages.error(request, "User already exists!")

    else:
        context = {
            "page": "active"
        }
        return render(request,'webapp/loginpage.html', context=context)

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email.split("@")[0], password=password)
        if user != None:
            login(request, user)
            return redirect('editor')
        return render(request, 'webapp/loginpage.html')


    else:
        return render(request, 'webapp/loginpage.html')

def search(request):
    about_query = Blog.objects.filter(about_icontains='sports')
    if (about_query).exists():
   
        return render(request, "webapp/blogpost.html")

def blogform(request):
    if request.method == 'POST':
        fm = BlogForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
            fm = BlogForm()    
    return render(request, "webapp/create.html", {'form':fm})

def about(request):
    return render(request, "webapp/about.html")   

def blogpage(request):
    return render(request, "webapp/blogpost.html")

def richeditor(request):
    return render(request, "webapp/text-editor.html")         
