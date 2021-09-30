from django.conf.urls import url
from .import views


urlpatterns = [
    
  url('calendar', views.CalendarView.as_view(), name='calendar'),
  url('register',views.event, name ='event_new'),
  url('register',views.event, name ='event_edit'),
]