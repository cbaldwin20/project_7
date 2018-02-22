
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings 
#from froala_editor.fields import FroalaField

def image_upload_path(instance, filename):
    return settings.MEDIA_ROOT

class Profile(models.Model):
    """info for profile page"""
    first_name = models.CharField(default="", max_length=255) 
    last_name = models.CharField(default="", max_length=255) 
    birthday = models.DateField(help_text="ex: mm/dd/yyyy")
    bio = models.CharField(default="", max_length=255) 
    city = models.CharField(default="", max_length=255, blank=True)
    state = models.CharField(default="", max_length=255, blank=True)
    country = models.CharField(default="", max_length=255, blank=True)
    favorite_animal = models.CharField(default="", max_length=255, blank=True)
    hobby = models.CharField(default="", max_length=255, blank=True)
    email = models.EmailField(default="", max_length=255)
    image = models.ImageField(upload_to='media')
    user = models.OneToOneField(User, blank=True, null=True, 
        related_name='the_profile', on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'User: ' + self.first_name + ' ' + self.last_name 