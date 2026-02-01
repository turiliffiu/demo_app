from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Quando si crea un nuovo User, crea automaticamente il suo UserProfile.
    Import di UserProfile fatto dentro la funzione per evitare import circolari.
    """
    if created:
        # Import lazy per evitare AppRegistryNotReady
        from .models import UserProfile
        UserProfile.objects.create(user=instance)
