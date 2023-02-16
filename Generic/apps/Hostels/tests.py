from django.test import TestCase
from rest_framework import status
from .models import Login, Hostel
from rest_framework.test import APITestCase
from django.urls import resolve
# Create your tests here.

# class AssignHostelTestCase(APITestCase):
#     def setUp(self):
#         self.user = Login.objects.create(
#             full_name="John Doe",
#             matric_no="MAT-12345",
#             gender = "MALE"
#         )
    
#     def test_assign_hostel(self):
#         url = f"hostel/assign_hostel/{self.user.id}/"
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data["message"], "Successfully assigned!")
#         hostel = Hostel.objects.get(assigned_to=self.user)
#         self.assertTrue(hostel.occupied)
        

class LogUserTestCase(APITestCase):
    def setUp(self):
        self.user = Login.objects.create(
            full_name="John Tester",
            matric_no= "P/ND/30/29380281",
            gender="MALE"
        )
        
    def test_login_user(self):
        url = "/hostel/login/"
        print(resolve(url))
        res_data = {
            "id": self.user.id,
            "full name": self.user.full_name,
            "matric_no": self.user.matric_no,
            "gender": self.user.gender,
        }
        response = self.client.post(url, res_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        res_data = {
            "id": self.user.id,
            "full name": self.user.full_name,
            "matric_no": self.user.matric_no,
            "gender": self.user.gender,
            "code": 201,
            "message": "Login Successful"
        }
        self.assertEqual(response.data, res_data)
