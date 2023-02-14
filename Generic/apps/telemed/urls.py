from django.urls import path
from . import views
from .views import CreatePatient

urlpatterns = [
    path("create/patient", CreatePatient.as_view(), name="create_patient")
]
