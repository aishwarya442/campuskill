from rest_framework import serializers
from .models import Test, TestAttempt
from users.serializers import AdminProfileSerializer, StudentProfileSerializer

class TestSerializer(serializers.ModelSerializer):
    admin = AdminProfileSerializer(read_only=True)
    
    class Meta:
        model = Test
        fields = '__all__'

class TestAttemptSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    test = TestSerializer(read_only=True)
    
    class Meta:
        model = TestAttempt
        fields = '__all__'

class TestAttemptCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAttempt
        fields = ('test', 'score')
