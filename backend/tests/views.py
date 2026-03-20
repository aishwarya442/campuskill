from rest_framework import generics, permissions
from .models import Test, TestAttempt
from .serializers import TestSerializer, TestAttemptSerializer, TestAttemptCreateSerializer
from users.permissions import IsStudent, IsAdminUser

class TestListView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user.admin_profile)

class TestAttemptCreateView(generics.CreateAPIView):
    queryset = TestAttempt.objects.all()
    serializer_class = TestAttemptCreateSerializer
    permission_classes = (IsStudent,)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user.student_profile)

class TestAttemptListView(generics.ListAPIView):
    serializer_class = TestAttemptSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return TestAttempt.objects.filter(student=user.student_profile)
        elif user.role == 'admin':
            return TestAttempt.objects.all()
        return TestAttempt.objects.none()
