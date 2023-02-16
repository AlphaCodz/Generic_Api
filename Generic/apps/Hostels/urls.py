from django.urls import path
from .views import LogUser, AssignHostel
from . import views

urlpatterns = [
    path("login/", LogUser.as_view(), name="login"),
    path("assign_hostel/<int:pk>/", AssignHostel.as_view(), name="assign_hostel")
]
