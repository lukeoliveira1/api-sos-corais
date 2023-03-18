from django.db import models

# Create your models here.
class Administrator(models.Model):
    username = models.CharField(max_length=30, unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)
  
    def __str__(self):
      return self.username 