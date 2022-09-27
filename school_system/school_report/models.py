from django.db import models
import uuid

class School(models.Model):
    name = models.CharField(max_length=20, null=False)
    max_student = models.IntegerField()


# Create your models here.
class Student(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    first_name = models.CharField(max_length=32, blank=True, null=False)
    last_name = models.CharField(max_length=32, blank=True, null=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
