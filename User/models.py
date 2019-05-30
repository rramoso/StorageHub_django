from django.db import models

# Create your models here.
class User(models.Model):

    username = models.CharField(primary_key=True,max_length = 200)
    name = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    role = models.CharField(max_length = 50)
    createdDate = models.DateTimeField(auto_now_add = True, blank=True)
