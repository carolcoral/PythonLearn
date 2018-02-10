from django.db import models
from email.policy import default


# Create your models here.

class Aritcle(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)
