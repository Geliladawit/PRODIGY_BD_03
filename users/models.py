from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    roles = models.CharField(max_length=20, default='user')