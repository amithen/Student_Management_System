from rest_framework import serializers
from .models import Student,Mark

class StudentSerializer(serializers.ModelSerializer):
    # reportingTeacher = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['id','name','age','gender','reportingTeacher','teachername']

    # def get_reportingTeacher(self,obj):
    #     return str(obj.reportingTeacher.teacherName)


class MarkSerializer(serializers.ModelSerializer):
    # studentName = serializers.SerializerMethodField()
    class Meta:
        model = Mark
        fields = ('id','studentName','studentname','termSelection','maths','science','history','totalMark','createdOn')

    # def get_studentName(self,obj):
    #     return str(obj.studentName.name)



