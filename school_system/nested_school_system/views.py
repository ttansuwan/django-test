from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from school_report.models import Student
from nested_school_system.serializers import StudentSerializer

# Create your views here.
class NestedStudentViewSet(ModelViewSet):
    serializer_class=StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])
