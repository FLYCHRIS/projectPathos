from django.urls import path
from . import views

app_name = "homePage"
urlpatterns = [
    path("home/", views.home, name='home'),
    path("home/plantAssist/", views.plantAssist, name='plantAssist')
]