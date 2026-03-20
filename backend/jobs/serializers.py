from rest_framework import serializers
from .models import Role, SelectionCriteria
from users.serializers import CompanyProfileSerializer

class SelectionCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectionCriteria
        exclude = ('role',)

class RoleSerializer(serializers.ModelSerializer):
    company = CompanyProfileSerializer(read_only=True)
    criteria = SelectionCriteriaSerializer(read_only=True)
    
    class Meta:
        model = Role
        fields = '__all__'

class RoleCreateSerializer(serializers.ModelSerializer):
    criteria = SelectionCriteriaSerializer(required=False)
    
    class Meta:
        model = Role
        fields = ('title', 'description', 'package', 'form_url', 'criteria')
        
    def create(self, validated_data):
        criteria_data = validated_data.pop('criteria', None)
        role = Role.objects.create(**validated_data)
        
        if criteria_data:
            SelectionCriteria.objects.create(role=role, **criteria_data)
        return role
