from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login_failed/', views.login, name='login_failed'),
    path('login_request/', views.login_request, name='login_request'),
    path('<int:pk>/', views.user_profile, name='user_profile'),
    path('<int:pk>/', views.user_profile, name='user_profile_elite'),
    path('<int:pk>/', views.user_profile, name='user_profile_lowelite'),
    path('<int:pk>/', views.user_profile, name='user_profile_high'),
    path('<int:pk>/', views.user_profile, name='user_profile_low'),
    path('promotion/<int:pk>/', views.user_profile_promotion, name="user_profile_promotion"),
    path('redemption/<int:pk>/', views.user_profile_redemption, name="user_profile_redemption")
]