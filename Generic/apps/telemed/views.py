from django.shortcuts import render
from .models import Patient
from .helpers.views import BaseView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response

class CreatePatient(BaseView):
    required_post_fields = ["first_name", "last_name", "email", "password"]
    
    def post(self, request, format=None):
        super().post(request, format)
        if Patient.objects.filter(email=request.data["email"]):
            res = {
                "code":400,
                "message": "Email is already taken"
            }
            return Response(res, 400)

        password = request.data.get("password")
        if not password:
            res = {
                "code": 400,
                "message": "Password Field Must Not Be Empty!"
            }
            return Response(res, 400)
        
        patient = Patient(email=request.data["email"])
        patient.first_name = request.data["first_name"]
        patient.last_name = request.data.get("last_name")
        patient.password = request.data["password"]
        hased_data = make_password(patient.password)
        patient.save()
        res = {
            "code":201,
            "message": "Account Created Successfully"
        }
        return Response(res, 201)