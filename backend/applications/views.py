from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Application
from .serializers import ApplicationSerializer, ApplicationCreateSerializer
from users.permissions import IsStudent
from rest_framework.exceptions import ValidationError

class ApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return Application.objects.filter(student=user.student_profile)
        elif user.role == 'company':
            return Application.objects.filter(role__company=user.company_profile)
        elif user.role == 'admin':
            return Application.objects.all()
        return Application.objects.none()

class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    permission_classes = (IsStudent,)

    def perform_create(self, serializer):
        student_profile = self.request.user.student_profile
        role = serializer.validated_data['role']
        
        # Check if already applied
        if Application.objects.filter(student=student_profile, role=role).exists():
            raise ValidationError("You have already applied for this role.")
            
        serializer.save(student=student_profile)
