from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'courses'
urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]