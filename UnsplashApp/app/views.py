from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import HDPhoto


def home(request):
    return render(request, 'app/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm-password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'app/signup.html', {'error': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'app/signup.html', {'error': 'Email already exists'})
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            return render(request, 'app/signup.html', {'error': "Password didn't exists"})
    return render(request, 'app/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('allphotos')
        return render(request, 'app/login.html', {'error': 'invalid credetial'})
    return render(request, 'app/login.html')


@login_required()
def dashboard(request):
    if request.method == 'POST':
        image = request.FILES['image']
        author = request.user
        print(author)
        user = HDPhoto(author=author, image=image)
        user.save()
        return redirect('dashboard')

    photos = HDPhoto.objects.filter(author=request.user)
    return render(request, 'app/dashboard.html', {'photos': photos})


def allphoto(request):
    photos = HDPhoto.objects.all()
    return render(request, 'app/photos.html', {'photos': photos})


def logout(request):
    auth.logout(request)
    return redirect('home')