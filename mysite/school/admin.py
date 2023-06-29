from django.contrib import admin
from .models import Facilitator, Student, Course, CourseStudent_Grade

# Register your models here.
admin.site.register(Facilitator)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseStudent_Grade)