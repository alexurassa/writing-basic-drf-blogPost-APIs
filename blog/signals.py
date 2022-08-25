import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Post


@receiver(post_save, sender=Post)
def set_post_publishment_status(created, sender, instance, **kwargs):
    if instance.published:
        instance.publishedAt = datetime.datetime.now()
        # instance.save()
    else:
        instance.publishedAt = None
