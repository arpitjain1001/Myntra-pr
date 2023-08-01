from django.shortcuts import render,HttpResponse

def login(request):
    return HttpResponse("this is login page")

def profile(request):
    return render(request,'index.html')

# Create your views here.
