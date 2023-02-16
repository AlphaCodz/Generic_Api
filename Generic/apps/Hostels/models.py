from django.db import models

# Create your models here.
class Login(models.Model):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    full_name = models.CharField(max_length=350)
    matric_no = models.CharField(max_length=25)
    gender = models.CharField(choices=GENDER, max_length=10)
    
    def __str__(self):
        return self.full_name
    
class Hostel(models.Model):
    user = models.OneToOneField(Login, on_delete=models.PROTECT)
    description_image1 = models.ImageField(upload_to="media/")
    hostel_description = models.TextField()
    
    occupied = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.full_name}"
    