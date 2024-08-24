from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField('Name', max_length=20, default='User')


    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    REQUIRED_FIELDS = []
