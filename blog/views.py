from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.messages.api import success
from django.shortcuts import render,HttpResponseRedirect
from . forms import LoginForm, PostForm, SignUpForm
from django.contrib import messages
from . models import Post


# home views
def home(request):
    posts= Post.objects.all()
    return render (request,'blog/home.html',{'posts':posts})


def about(request):
    return render (request,'blog/about.html')


def contact(request):
    return render (request,'blog/contact.html')


#Dashboard View
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        return render (request,'blog/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')


#Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


#Sign Up View
def signup(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations!! You have Become an Author")
            form.save()
    else:
        form= SignUpForm()
    return render (request,'blog/signup.html',{'form':form})

#Login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form= LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user =authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in Successfully!!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form= LoginForm()
        return render (request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


#Add View 
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=PostForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            form= PostForm()
        return render (request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


#Update/Edit View
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi= Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi= Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render (request,'blog/update.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')



#Delete View
def delete_post(request,id ):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi= Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')