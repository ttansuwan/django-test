from school_report.models import School, Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'school_pk': 'school__pk',
    }
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
        }

    
    def create(self, validated_data):
        school_id = validated_data['school'].id
        school_max = validated_data['school'].max_student
        total_student = Student.objects.filter(school_id=school_id).count()
        if total_student < school_max:
            new_student = Student()
            new_student.first_name = validated_data['first_name']
            new_student.last_name = validated_data['last_name']
            new_student.school = validated_data['school']
            new_student.save()
            return new_student
        else:
            raise serializers.ValidationError("This school is full")
        