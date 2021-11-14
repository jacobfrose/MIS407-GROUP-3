from django.urls import path
from promotion import views

urlpatterns = [
    path('', views.promotion, name='promotion'),
]