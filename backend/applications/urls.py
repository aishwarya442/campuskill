from django.urls import path
from .views import ApplicationListView, ApplicationCreateView

urlpatterns = [
    path('', ApplicationListView.as_view(), name='application-list'),
    path('apply/', ApplicationCreateView.as_view(), name='application-create'),
]
