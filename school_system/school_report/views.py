from django.shortcuts import render
from school_report.models import School, Student
from rest_framework.viewsets import ViewSet
from rest_framework import permissions
from rest_framework.response import Response

from school_report.daos import get_students
from school_report.serializers import SchoolSerializer, StudentSerializer

# Create your views here.
class StudentViewSet(ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        serializer = StudentSerializer(get_students(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None):
        serializer = StudentSerializer((get_students(student_id=id)))
        return Response(serializer.data)
    
class SchoolViewSet(ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = School.objects.all()
    permission_classes = [permissions.IsAuthenticated]