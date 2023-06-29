from django.urls import path
from .views import CourseAPIView, StudentAPIView, FacilitatorAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("home/", views.home, name="home"),
path("student/", views.student, name="student"),
path("facilitator/", views.facilitator, name="facilitator"),
path("courses/", views.courses, name="courses"),
path("yourcourses/", views.yourcourses, name="yourcourses"),
path("enroll/",views.enroll, name="enroll"),
path('api/course/', CourseAPIView.as_view(), name='course-api'),
path('api/student/', StudentAPIView.as_view(), name='student-api'),
path('api/facilitator/', FacilitatorAPIView.as_view(), name='facilitator-api'),
]