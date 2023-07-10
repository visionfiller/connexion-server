from django.db import models
from django.contrib.auth.models import User


class ConnexionUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250)
    profile_picture = models.CharField(max_length=250)
    orientation = models.ForeignKey("Orientation",on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey("Gender",on_delete=models.CASCADE, null=True)
    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'