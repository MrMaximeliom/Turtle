from django.db.models.signals import post_save
from .models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
         new_profile = Profile.objects.create(user=instance)
         if instance.gender == 'Male':
             new_profile.image = "/profile_pics/default_male.jpg"
         else:
            new_profile.image = "/profile_pics/default_female.jpg"


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()