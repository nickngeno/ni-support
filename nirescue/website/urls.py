from django.urls import path
from . import views

# urlpatterns go her
urlpatterns = [
    path('',views.home , name="home"),
    path('about_us.html', views.about_us, name="about_us"),
    path('blog.html', views.blog, name="blog"),
]