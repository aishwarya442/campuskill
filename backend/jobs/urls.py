from django.urls import path
from .views import RoleListView, RoleDetailView, RoleCreateView

urlpatterns = [
    path('', RoleListView.as_view(), name='role-list'),
    path('create/', RoleCreateView.as_view(), name='role-create'),
    path('<int:pk>/', RoleDetailView.as_view(), name='role-detail'),
]
