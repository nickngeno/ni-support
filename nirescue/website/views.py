from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# about us page
def about_us(request):
    return render(request, 'about_us.html')

# blog page goes here
def blog(request):
    return render(request, 'blog.html')