from django.urls import path
from .views import AppoimentsCreateView, AppoimentsUpdateView

urlpatterns = [
    path("", AppoimentsCreateView.as_view(), name="appoiments"),
    path("<int:pk>/editar/", AppoimentsUpdateView.as_view(), name="update_appoiments"),
]
