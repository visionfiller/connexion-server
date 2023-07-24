from django.db import models


class FriendRequest(models.Model):
    connexion_user_from = models.ForeignKey("ConnexionUser", on_delete=models.CASCADE, related_name="request_sender")
    connexion_user_to = models.ForeignKey("ConnexionUser", on_delete=models.CASCADE, related_name="request_receiver")
    status = models.CharField(max_length=100)

    
   