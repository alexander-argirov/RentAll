from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from RentAll.accounts.models import Profile, RentAllUser
from django.core.mail import send_mail

UserModel = get_user_model()


def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Website'
        html_message = render_to_string('common/welcome_email.html', {'user': instance})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = instance.email
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if not created:
        return
    send_welcome_email(sender, instance, created)

    Profile.objects.create(user=instance)
