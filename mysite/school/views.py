from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course, CourseStudent_Grade, Student, Facilitator
from .serializers import CourseSerializer, StudentSerializer, FacilitatorSerializer
from rest_framework import authentication, permissions, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(response):
    return render(response, "school/base.html",{})

def home(response):
    return render(response, "school/home.html",{})

def student(response):
    response.user
    return render(response, "school/student.html",{})

def facilitator(response):
    return render(response, "school/facilitator.html",{})

def courses(response):
    student = response.user.student
    courses = Course.objects.exclude(courseCourse__student=student)
    context = {
        'courses' : courses
    }
    return render(response, "school/courses.html",context)

def yourcourses(response):
    student = response.user.student
    courses = CourseStudent_Grade.objects.filter(student=student)
    context = {
            'courses' : courses
        }
    return render(response, "school/yourcourses.html",context)

def enroll(response):
    if (response.method == 'POST' and response.user.is_authenticated):
        course_id = response.POST.get('courseId')
        course = Course.objects.get(id=course_id)
        student = response.user.student

        CourseStudent_Grade.objects.create(course=course, student=student)

        return redirect('/courses/')


    return redirect('/student/')

class CourseAPIView(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

class StudentAPIView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

class FacilitatorAPIView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get(self, request):
        queryset = Facilitator.objects.all()
        serializer = FacilitatorSerializer(queryset, many=True)
        return Response(serializer.data)