from django.contrib import admin
from .models import Student, School
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
admin.site.register(Student)
admin.site.register(School)
TokenAdmin.raw_id_fields = ['user']