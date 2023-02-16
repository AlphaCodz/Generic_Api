from django.urls import path
from .views import LogUser
from . import views

urlpatterns = [
    path("login/", LogUser.as_view(), name="login"),
    path("assign_hostel/<int:pk>/", views.assign_hostel, name="assign_hostel")
]
