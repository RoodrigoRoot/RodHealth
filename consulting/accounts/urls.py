from django.urls import path
from .views import *



urlpatterns = [
    #Doctor
    path("cuenta/<slug:slug>/", DoctorDetailView.as_view(), name="account"),
    path("cuenta/<int:pk>/edit", DoctorUpdateView.as_view(), name="account_update"),

    #Patient
    path("paciente/list/", PatientListView.as_view(), name="list_patients"),
    path("paciente/create/", PatientsCreateView.as_view(), name="create_patient"),
    path("paciente/<int:pk>/edit/", PatientUpdateView.as_view(), name="update_patient"),
    path("paciente/<int:pk>/del/", PatientDeleteView.as_view(), name="del_patient"),
    path("paciente/<slug:slug>/detail/", PatientDetailView.as_view(), name="detail_patient"),

    #IN-OUT
    path("salir/", logout_view, name="logout"),
]
