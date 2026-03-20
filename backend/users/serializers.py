from rest_framework import serializers
from .models import User, AdminProfile, CompanyProfile, StudentProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        exclude = ('user',)

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        exclude = ('user',)

class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        exclude = ('user',)

class UserSerializer(serializers.ModelSerializer):
    student_profile = StudentProfileSerializer(read_only=True)
    company_profile = CompanyProfileSerializer(read_only=True)
    admin_profile = AdminProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'role', 'student_profile', 'company_profile', 'admin_profile')

class RegisterSerializer(serializers.ModelSerializer):
    # Additional fields from frontend Register.jsx
    name = serializers.CharField(write_only=True)
    collegeName = serializers.CharField(write_only=True, required=False)
    phone = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ('email', 'password', 'role', 'name', 'collegeName', 'phone')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        name = validated_data.pop('name')
        college_name = validated_data.pop('collegeName', '')
        phone = validated_data.pop('phone', '')
        
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        
        # Create corresponding profile
        if user.role == 'student':
            StudentProfile.objects.create(
                user=user, 
                name=name, 
                college_name=college_name, 
                phone=phone
            )
        elif user.role == 'company':
            CompanyProfile.objects.create(user=user, name=name)
        elif user.role == 'admin':
            AdminProfile.objects.create(user=user, name=name)
            
        return user
