from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_verified = models.BooleanField(default=False)
    sex_choice = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('N', 'None',)
    )
    sex = models.CharField(max_length=1, choices=sex_choice)
    attempts = models.CharField(max_length=100, blank=True)
    highest = models.BigIntegerField(blank=True, default=0)
    mobile = models.IntegerField(blank=True)
    image = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return "{0} {1} with username {2}".format(self.firstname, self.lastname, self.username)

