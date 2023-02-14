from django.shortcuts import render
from .helpers.views import BaseView
from .models import Login
from rest_framework.response import Response

# Create your views here.
class LogUser(BaseView):
    required_post_fields = ["full_name", "matric_no", "gender"]
    
    def post(self, request, format=None):
        super().post(request, format)
        
        user = Login.objects.create(
            full_name = request.data["full_name"],
            matric_no = request.data["matric_no"],
            gender = request.data["gender"]
        )
        user.save()
        res_data = {
            "code": 201,
            "message": "Login Successful"
        }
        return Response(res_data, 201)
        