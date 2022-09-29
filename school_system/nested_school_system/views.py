from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from school_report.models import Student, School
from rest_framework.permissions import AllowAny
from nested_school_system.serializers import StudentSerializer
from school_system.paginations import CustomPagination

# Create your views here.
class NestedStudentViewSet(ModelViewSet):
    serializer_class=StudentSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])