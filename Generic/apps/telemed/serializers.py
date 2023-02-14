from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
   class Meta:
       model=Patient
       fields = ("first_name", "last_name", "email", "password")
       
   def create(self, validated_data):
        patients = Patient.objects.create(
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"],
            password = validated_data["password"]
        )
        patients.set_password(raw_password=validated_data["password"])
        patients.save()
        return patients