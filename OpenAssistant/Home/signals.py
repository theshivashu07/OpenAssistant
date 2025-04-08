from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse

User = get_user_model()

@receiver(user_signed_up)
def after_signup(request, user, **kwargs):
    """ Handle new user signup """
    user.is_new = True  # Custom attribute to identify a new user
    user.save()
