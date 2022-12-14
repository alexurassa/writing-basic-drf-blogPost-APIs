from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User 

from .models import Profile

@receiver(post_save, sender=User, weak=False)
def signal_receiver(created, sender, instance, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
