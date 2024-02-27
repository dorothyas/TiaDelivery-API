from django.db import models
from user.models import CustomUser

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    # img = models.ImageField()    cover_photo = models.ImageField(upload_to='covers/', null=True, blank=True)
    # seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='notes')
    
