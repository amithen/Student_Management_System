from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


class Teacher(models.Model):
    teacherName = models.CharField(max_length=20)
    def __str__(self):
        return self.teacherName

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    genderChoice = [
        ('MALE','M'),
        ('FEMALE','F'),
        ('OTHERS','OTHERS'),
    ]

    gender = models.CharField(choices=genderChoice,max_length=10)
    reportingTeacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    @property
    def teachername(self):
        return self.reportingTeacher.teacherName

    def __str__(self):
        return self.name

class Mark(models.Model):
    studentName = models.ForeignKey(Student,on_delete=models.CASCADE)
    termSelectionChoice = [
        ('one', 'One'),
        ('two', 'Two'),
    ]
    termSelection = models.CharField(max_length=5,choices=termSelectionChoice)
    maths = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(100)])
    science = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(100)])
    history = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(100)])
    createdOn = models.DateTimeField()

    @property
    def studentname(self):
        return self.studentName.name

    @property
    def totalMark(self):
        totalMark = self.maths+self.science+self.history
        return totalMark

    def __str__(self):
        return self.studentName.name


