from django.urls import path
from redemption import views

urlpatterns = [
    path('', views.redemption, name='redemption'),
]