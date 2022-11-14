from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.Info(request, "invalid details")
            return redirect('login')

    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.Info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.Info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=name, username=username, email=email, password=password1)
                user.save();
                print('user created')
                return redirect('login')
        else:
            print("password not matched")
    else:
        return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
