# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

# Create your models here.


class ProfileManager(models.Manager):
    def toggle_follow(self, request_user, username_to_toggle):
        profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = request_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return is_following


class Profile(models.Model):
    # grabs user.profile reverse
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User, related_name='is_following', blank=True)
    # following = models.ManyToManyField(User, related_name='following', blank=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        print("Activation")
        pass


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
        default_user_profile.followers.add(instance)
        # with many to many fields, there is no need for: default_user_profile.save()
        profile.followers.add(default_user_profile.user)
        profile.followers.add(2)


post_save.connect(post_save_user_receiver, sender=User)

