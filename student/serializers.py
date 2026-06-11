from rest_framework import serializers
from student.models import *


class AssignmentSerializer(serializers.Serializer):
    title=serializers.CharField()
    description=serializers.CharField()
    added_at=serializers.DateTimeField(read_only=True)
    submission_date=serializers.DateField()

class TodoSerializer(serializers.Serializer):
    title=serializers.CharField()
    description=serializers.CharField()
    subject=serializers.CharField()
    added_date=serializers.DateTimeField(read_only=True)

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields="__all__"
        read_only_fields=["added_date"]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"

