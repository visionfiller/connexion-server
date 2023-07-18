from django.db import models



class Post(models.Model):
    body = models.TextField(max_length=150)
    image = models.CharField(max_length=50)
    connexion_user = models.ForeignKey("ConnexionUser", on_delete=models.CASCADE)
 
   