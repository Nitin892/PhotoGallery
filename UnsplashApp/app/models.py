from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class HDPhoto(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')
    created_on = models.DateTimeField(auto_now_add=True)
