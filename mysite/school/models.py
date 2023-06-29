from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Facilitator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="facilitator", null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
            return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student", null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    index = models.IntegerField()

    def __str__(self):
            return self.name

class Course(models.Model):
    name = models.CharField(max_length=250)
    hours = models.IntegerField()
    facilitator = models.ForeignKey(Facilitator, on_delete=models.CASCADE, related_name="courseFacilitator", null=True)

    def __str__(self):
            return self.name

class CourseStudent_Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courseCourse", null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="courseStudent", null=True)
    grade = models.IntegerField(null=True)

    def __str__(self):
            return self.course.name + ' indeks: ' + str(self.student.index)