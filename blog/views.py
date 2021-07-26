from django import forms
from django.shortcuts import render,HttpResponseRedirect
from . forms import SignUpForm


# home views
def home(request):
    return render (request,'blog/home.html')


def about(request):
    return render (request,'blog/about.html')


def contact(request):
    return render (request,'blog/contact.html')

def dashboard(request):
    return render (request,'blog/dashboard.html')

def user_logout(request):
   return HttpResponseRedirect('/')

def signup(request):
    form= SignUpForm()
    return render (request,'blog/signup.html',{'form':form})


def login(request):
    return render (request,'blog/login.html')