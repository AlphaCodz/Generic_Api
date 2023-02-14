from django.urls import path
from . import views
from .views import CreatePatient, GetAllPatients


urlpatterns = [
    path("create/patient", CreatePatient.as_view(), name="create_patient"),
    path("get/all/patient", GetAllPatients.as_view(), name="get_patients")
]
