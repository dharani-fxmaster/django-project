from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),  
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register'),
    path('list/', views.RegisterListView.as_view(), name="list"),
    path('create/', views.RegisterCreateView.as_view(), name="create"),
    path('update/<int:pk>/', views.RegisterUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', views.RegisterDeleteView.as_view(), name="delete"),
    # path('list/', views.RegisterListView.as_view(), name='list_page'),
    path('result/', views.ResultView.as_view(), name='result_view'),
    
    path('result-page/', views.result_view, name='result_page'),

]