from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 



# Create your views here.
def index(request):
    return render(request,'core/index.html')

def contact (request):
    return render(request, 'core/contact.html')

def reservation(request):
    return render(request,'core/reservations.html')

def driver (request):
    return render(request,'core/driver.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3:
            messages.error(request, 'Password must be at least 5 characters')
            return redirect('register')

        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request, 'Use another username')
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request,'User successfully created, login now')
        return redirect('login')
    return render(request,'core/register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')    
        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('reservation')
        else:
            messages.error(request, 'wrong user details')
            return redirect('login')


                      
    return render(request,'core/login.html')


def reservation(request):
    return render(request,'core/reservations.html')