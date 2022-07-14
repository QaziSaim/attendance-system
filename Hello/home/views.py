from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def login(request):
    return render(request,'login.html')
    # return render(request,'about.html')
    # return HttpResponse("This is about page")
def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is services page")