from rest_framework import viewsets
from .serializers import StudentSerializer,MarkSerializer
from .models import Student,Teacher,Mark


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

