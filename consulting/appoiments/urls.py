from django.urls import path
from .views import AppoimentsCreateView

urlpatterns = [
    path("", AppoimentsCreateView.as_view(), name="appoiments")
]
