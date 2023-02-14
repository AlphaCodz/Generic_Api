from django.urls import path
from .views import LogUser

urlpatterns = [
    path("login/", LogUser.as_view(), name="login")
]
