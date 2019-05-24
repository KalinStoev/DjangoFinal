from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='user-profile'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),


]