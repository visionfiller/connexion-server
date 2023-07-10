from django.db import models



class Orientation(models.Model):
    label = models.TextField(max_length=25)
 
   