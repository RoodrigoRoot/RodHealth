from django.urls import path
from .views import AppoimentView

urlpatterns = [
    path("", AppoimentView.as_view(), name="appoiments")
]
