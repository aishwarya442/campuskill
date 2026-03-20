from rest_framework import generics, permissions
from .models import Role
from .serializers import RoleSerializer, RoleCreateSerializer
from users.permissions import IsCompanyOrAdmin

class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAuthenticated,)

class RoleDetailView(generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAuthenticated,)

class RoleCreateView(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleCreateSerializer
    permission_classes = (IsCompanyOrAdmin,)

    def perform_create(self, serializer):
        # Assign company profile if the user is a company
        user = self.request.user
        if user.role == 'company':
            serializer.save(company=user.company_profile)
        else:
            # If admin, maybe pass company_id in request. But for now, require it in payload
            serializer.save()
