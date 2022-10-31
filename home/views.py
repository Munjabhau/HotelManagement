from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def register_attempt(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        try:
            if User.objects.filter(username=username).first():
                messages.error(request, 'username is allready taken')
                return redirect('/register_attempt')

            if User.objects.filter(email=email).first():
                messages.error(request, 'email is allready taken')
                return redirect('/register_attempt')

            if len(username) < 4 or len(email) < 4 or len(fname) < 2 or len(lname) < 2 or len(pass1) < 4:
                messages.error(request, 'Please fill the details correctly')
            else:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.set_password(pass1)
                myuser.save()
                messages.success(request, 'Account created successfully')
                return redirect('/login_attempt')
        except Exception as e:
            print(e)
    return render(request, 'home/register.html')


def login_attempt(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            print("user not fount")
            return redirect('/login_attempt')
        user = authenticate(username=username, password=password)
        if user is None:
            print("Wrong password")
            return redirect('/login_attempt')
        login(request, user)
        messages.success(request, "Login successfully")
        return redirect('/')
    return render(request, 'home/login.html')


def logout_attempt(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('/login_attempt')
