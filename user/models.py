from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=255, blank=True )
    # cover_photo = models.ImageField(upload_to='covers/', null=True, blank=True)