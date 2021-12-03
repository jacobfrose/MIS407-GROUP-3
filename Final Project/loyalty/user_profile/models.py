from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    birthday = models.TextField(max_length=20)
    address = models.TextField(max_length=100)
    totalpoints = models.TextField(max_length=10)
    pointsearned = models.TextField(max_length=10)