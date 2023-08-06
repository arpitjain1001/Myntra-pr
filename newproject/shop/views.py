from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required



@login_required(login_url="/shop/log/")
def profile(request):
    return render(request,'indes.html')


def register(request):
     if request.method == "POST":
          username =  request.POST.get('username')
          password =  request.POST.get('password') 

          user = User.objects.filter(username=username) 
          
          if user.exists():
               messages.error(request, "username already exist.")
               return redirect('/shop/register/')


          user = User.objects.create(username=username)
          
          user.set_password(password)
          user.save()
          messages.success(request, "account registerd.")
          return redirect("/shop/log/")

     return render(request,'register.html')    

def log(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        if not User.objects.filter(username=username).exists(): #sbse phele yeh search krega
            messages.error(request, "Invalid username")
            return redirect("/shop/log/")

        user = authenticate(username=username, password=password)

        if user is not None:  
            messages.success(request, "You are a user.")
            login(request, user=user)
            return redirect('/shop/')
        else:
            messages.error(request, "You are not a user and username and password are incorrect.")
            return render(request, "log.html")
    return render(request, "log.html")

def logoutuser(request):
    logout(request)
    return render(request,"log.html")

def test(request):
    return render(request,"test.html ")




