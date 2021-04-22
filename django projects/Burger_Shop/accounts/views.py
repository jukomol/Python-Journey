from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def regform(request):

    if request.method == 'POST':
        username= request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('regform')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('regform')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('signin')

        else:
            messages.info(request,'Password not matching')
            return redirect('regform')
        return redirect('/')
    else:
        return render(request,'regform.html',{})
def signin(request):
    if request.method== 'POST':
        username= request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('signin')

    else:
        return render(request,'signin.html')
    return render(request,'signin.html',{})

def logout(request):
    auth.logout(request)
    return redirect("/")

def user(request):
    return render(request,'user.html',{})

def user_management(request):
    return render(request,'user_management.html',{})

def food_management(request):
    return render(request,'food_management.html',{})

def order_management(request):
    return render(request,'order_management.html',{})

