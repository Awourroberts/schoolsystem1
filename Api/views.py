from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from  cal.models import Event
from .serializers import StudentSerializer
from .serializers import TrainerSerializer
from .serializers import CoursesSerializer
from .serializers import EventsSerializer



class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset =Event .objects.all()
    serializer_class=EventsSerializer







