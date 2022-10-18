from rest_framework import serializers
from ..models import Subject
from ..models import Course, Module

class SubjectSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Subject
        fields = ['id', 'title']
    
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']

class CourseSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'overview', 'created', 
                    'owner', 'Module']