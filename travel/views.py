from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def signupPage(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if (password != repassword):
            messages.error(request, "Passwords do not match.")
            return redirect('/signupPage/')
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(
            request, "Your account has been successfully created. You are logged in now.")
        login(request, myuser)
        return redirect('/tour/')
    else:
        return render(request, 'signupPage.html')


def loginPage(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            messages.success(request, "Successfully Logged In")
            login(request, user)
            return redirect('/tour/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/loginPage/')

    else:
        return render(request, 'loginPage.html')


def logoutPage(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')
