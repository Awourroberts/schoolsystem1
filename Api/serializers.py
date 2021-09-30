from django.db import models
from django.db.models import fields
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from cal .models import Event



class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age")

class TrainerSerializer (serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name","last_name","age")

class CoursesSerializer (serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=("course_Name","course_","course_Title")

class EventsSerializer (serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=("course_Name","course_","course_Title")

