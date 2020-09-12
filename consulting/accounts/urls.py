from django.urls import path
from .views import logout_view, DoctorUpdateView, PatientsCreateView, UpdatePatient

urlpatterns = [
    path("cuenta/<int:pk>/", DoctorUpdateView.as_view(), name="account"),
    path("pacientes/", PatientsCreateView.as_view(), name="patients"),
    path("pacientes/<int:pk>/editar/", UpdatePatient.as_view(), name="update_patients"),
    path("salir/", logout_view, name="logout"),
]
