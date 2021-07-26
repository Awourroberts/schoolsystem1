from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    date_of_birth=models.DateField()
    age=models.PositiveSmallIntegerField()
    rolenumber=models.CharField(max_length=12)
    district=models.CharField(max_length=12)
    gender=models.CharField(max_length=12)
    email=models.EmailField(max_length=12)
    student_id=models.PositiveSmallIntegerField()
    nationality=models.CharField(max_length=12)
    national_id=models.CharField(max_length=12)
    medical_report=models.CharField(max_length=12)
    language=models.CharField(max_length=15)
    laptopserialnumber=models.CharField(max_length=15)
    date_of_enrollment=models.DateField()
    profile=models.ImageField()
    phone_number=models.CharField(max_length=12)
# Create your models here.
