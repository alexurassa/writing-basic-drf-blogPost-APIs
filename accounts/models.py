from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        max_length=300, upload_to="avatars/", null=False, default="avatars/default.jpeg"
    )
    description = models.TextField(
        max_length=300, default="No profile description yet."
    )

    def __str__(self):
        return f"{self.user.username} profile"
    
    
    def _get_default_profile_description(self):
        if self.description is None or self.description == "":
            return f"{self.user.username} has not uploaded profile description yet."
