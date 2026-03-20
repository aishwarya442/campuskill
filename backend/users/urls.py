from django.urls import path
from .views import (
    RegisterView, CustomTokenObtainPairView, 
    UserProfileView, CompanyListView, CompanyDetailView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('me/', UserProfileView.as_view(), name='user-profile'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
]
