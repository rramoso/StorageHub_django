from django.db import models

# Create your models here.
class User(models.Model):

    username = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200)
