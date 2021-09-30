from django.db import models

class Courses(models.Model):
    course_name=models.CharField(max_length=20,null=True)
    trainer=models.CharField(max_length = 20,null=True)
    course_code=models.CharField(max_length = 50,null=True)
    syllabus=models.FileField(upload_to ='documents/',null=True)
    description=models.TextField(blank=True,null=True)
    course_schudule=models.SmallIntegerField()
    assignment=models.CharField(max_length = 50,null=True)

# Create your models here.
