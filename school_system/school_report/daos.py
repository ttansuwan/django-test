from school_report.models import School, Student
from django.shortcuts import get_object_or_404

def get_students(student_id=None):
    try:
        if student_id is not None:
            students = Student.objects.get(id=student_id)
        else:
            students = Student.objects.all()
    except Student.DoesNotExist:
        students = None
    return students
    
def get_school(school_id=None):
    try:
        if school_id is not None:
            schools = School.objects.get(id=school_id)
        else:
            schools = School.objects.all()
    except School.DoesNotExist:
        schools = None
    return schools
    