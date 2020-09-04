from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("entrar/", LoginView.as_view(), name="loguin"),
]
