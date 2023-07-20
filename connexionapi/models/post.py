from django.db import models
from django.utils import timezone
from django.template.defaultfilters import date as date_filter




class Post(models.Model):
    body = models.TextField(max_length=150)
    image = models.CharField(max_length=50)
    connexion_user = models.ForeignKey("ConnexionUser", on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, null=True, blank=True)
    @property
    def formatted_date(self):
        return date_filter(self.date_created, "Y-m-d h:i A")
   