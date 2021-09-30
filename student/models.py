from django.db import models

class Student(models.Model):
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    first_name=models.CharField(max_length=12,null=True)
    last_name=models.CharField(max_length=12,null=True)
    date_of_birth=models.DateField(null=True)
    age=models.PositiveSmallIntegerField(null=True)
    district=models.CharField(max_length=12,null=True)
    gender_choices=(
        ('1','Famale'),
        ('2','Male'),
        ('3','Other') )
   
    gender=models.CharField(max_length=12,choices=gender_choices)
    email=models.EmailField(max_length=30,null=True)
    student_id=models.PositiveSmallIntegerField(null=True)
    NATIONALITY_OPTIONS=(
        ('1','kenya'),
        ('1','Rwanda'),
        ('1','uganda')

    )
    nationality=models.CharField(max_length=17,choices=NATIONALITY_OPTIONS,null=True)
    national_id=models.CharField(max_length=12,null=True)
    medical_report=models.FileField(upload_to='files/',null=True)
    language=models.CharField(max_length=15,null=True)
    laptop_serial_number=models.CharField(max_length=15,null=True)
    date_of_enrollment=models.DateField(null=True)
    profile_picture=models.ImageField(upload_to ='image/',null=True)
    phone_number=models.CharField(max_length=12,null=True)
    role_number=models.CharField(max_length=12,null=True)
   