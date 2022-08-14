from django.urls import path
from . import views

app_name = "plantAssist"
urlpatterns = [
    path("plant-procedures/", views.PAMenu, name='PAMenu')
]