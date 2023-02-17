from django.shortcuts import render, get_object_or_404
from .helpers.views import BaseView
from .models import Login, Hostel
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Login


# Create your views here.
class LogUser(BaseView):
    required_post_fields = ["id", "full_name", "matric_no", "gender"]
    
    def post(self, request, format=None):
        super().post(request, format)
        
        data = request.data["matric_no"]
        matric_no = Login.objects.get_or_create(matric_no=data)
        
        user = Login.objects.create(
            full_name = request.data["full_name"],
            matric_no= matric_no,
            gender = request.data["gender"]
        )
        user.save()
        res_data = {
            "id": user.id,
            "full name": user.full_name,
            "matric_no": user.matric_no,
            "gender": user.gender,
            "code": 201,
            "message": "Login Successful"
        }
        return Response(res_data, 201)
    
    

# class AssignHostel(APIView):
def assign_hostel(self, request, pk):
    user = get_object_or_404(Login, pk=id)
    if not user:
        res_data = {
            "code": 404,
            "message": "Sorry, you're not an identified student of YCT. Please log in."
        }
        return Response(res_data, status=404)
    hostel = Hostel(assigned_to=user)
    hostel.occupied = True
    hostel.save()
    res_data = {
        "message": "Successfully assigned!"
    }
    return Response(res_data, status=status.HTTP_201_CREATED)
           
    