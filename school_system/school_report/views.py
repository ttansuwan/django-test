from django.shortcuts import render
from school_report.models import School, Student
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from school_system.paginations import CustomPagination

from school_report.daos import get_students
from school_report.serializers import SchoolSerializer, StudentSerializer

# Create your views here.
class StudentViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]
    
class SchoolViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]