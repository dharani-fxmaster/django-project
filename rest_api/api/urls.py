from django.urls import path
from .import views

urlpatterns = [
    path('students/',views.StudentsViews),
    path('students/<int:pk>/',views.StudentDetailView),
    path('employee/', views.Employees.as_view()),
    path('employee/<int:pk>/',views.EmployeeDetail.as_view()),
]