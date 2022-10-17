from rest_framework import serializers
from ..models import Subject
from ..models import Course, Classes

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title']
    
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['order', 'title', 'description']

class CourseSerializer(serializers.ModelSerializer):
    classes = ClassesSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'overview', 'created', 
                    'owner', 'classes']