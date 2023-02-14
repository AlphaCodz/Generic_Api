from django.shortcuts import render
from .models import Patient
from .helpers.views import BaseView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from .serializers import PatientSerializer
from django.contrib.auth.hashers import make_password

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
        
        patient = Patient.objects.create(
            email = request.data.get("email"),
            first_name = request.data["first_name"],
            last_name = request.data.get("last_name"),
            )
        patient.password = make_password(request.data["password"])
        patient.save()
        res = {
            "code":201,
            "message": "Account Created Successfully"
        }
        return Response(res, 201)
    

# class GetPatients(BaseView):
#     required_get_fields = ["first_name", "last_name", "email", "password"]
#     def post(self, request, format=None):
#         super().post(request, format)
#         first_name = request.query_params.get('first_name')
#         last_name = request.query_params.get('last_name')
#         email = request.query_params.get('email')
        
#         patients = Patient.objects.all()
#         if first_name:
#             patients = patients.filter(first_name=firstname)
#         if last_name:
#             patients = patients.filter(last_name=last_name)
#         if email:
#             patients = patients.filter(email=email)
            
#         patient_list = []
#         for patient in patients:
#             patient_dict = {
#                 "id": patient.id,
#                 "first_name": patient.first_name,
#                 "last_name": patient.last_name,
#                 "email": patient.email,
#                 "password": patient.password
#             }
#             patient_list.append(patient_dict)
        
#         res = {
#             "code": 200,
#             "data": patient_list
#         }
#         return JsonResponse(res, status=200)

class GetAllPatients(APIView):
    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)