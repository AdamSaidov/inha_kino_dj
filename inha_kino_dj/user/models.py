from django.db import models
from rest_framework import permissions


class User(models.Model):
    username = models.CharField(max_length=150, null=True)
    first_name = models.TextField(max_length=150, blank=True)
    last_name = models.TextField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, null=True)
    password = models.CharField(max_length=50, null=True)
    user_permissions = models.ManyToManyField
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.
    date_joined = models.
