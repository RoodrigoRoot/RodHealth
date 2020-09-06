from django.urls import path
from .views import MyAccountView, logout_view,UpdateUser

urlpatterns = [
    path("<int:pk>/", UpdateUser.as_view(), name="account"),
    path("salir/", logout_view, name="logout"),
]
