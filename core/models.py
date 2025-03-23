from django.db import models

# Create your models here.

class React(models.Model):
    name = models.CharFiled(max_length=30)
    detail = model.CharField(max_length=500)
