from django.shortcuts import render, get_object_or_404
from .helpers.views import BaseView
from .models import Login, Hostel
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
    
    
def AssignHostel(request, id):
    user = get_object_or_404(Login, pk=id)
    hostel = Hostel(assigned_to=user)
    hostel.save()
    res = {
        "hostel":hostel
    }
    return Response({"message": "Successfully Assigned!"}, 201)
   
    # hostel_name = request.data["name"]
    # hostel = Hostel.objects.get(hostel_name)
    # user = Hostel.objects.get(assigned_to__pk=id)
    # if user.paid == True:
    #     user.occupied == True
    #     return Response({"message": "User Assigned to "})
    # return False
           
    