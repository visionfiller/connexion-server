from django.db import models

class Gender(models.Model):
    label = models.TextField(max_length=25)
 
   