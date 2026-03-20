from rest_framework import serializers
from .models import Application
from users.serializers import StudentProfileSerializer
from jobs.serializers import RoleSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    role = RoleSerializer(read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('role',)
