from django.db import models

# Create your models here.

class feedback(models.Model):
    fb_name=models.CharField(max_length=40)
    fb_phone=models.CharField(max_length=12)
    fb_comment=models.TextField()