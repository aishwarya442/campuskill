from django.urls import path
from .views import TestListView, TestAttemptListView, TestAttemptCreateView

urlpatterns = [
    path('', TestListView.as_view(), name='test-list'),
    path('attempts/', TestAttemptListView.as_view(), name='test-attempt-list'),
    path('<int:pk>/attempt/', TestAttemptCreateView.as_view(), name='test-attempt-create'),
]
