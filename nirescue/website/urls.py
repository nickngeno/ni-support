from django.urls import path
from . import views

# urlpatterns go her
urlpatterns = [
    path('',views.home , name="home"),
]