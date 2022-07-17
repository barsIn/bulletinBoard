from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from django.template.loader import render_to_string
from dotenv import load_dotenv
from django.core.mail import send_mail
import os
from .models import Advertisement, Response


load_dotenv()


@receiver(post_save, sender=Response)
def check(sender, instance, **kwargs):
    subject = f'{instance.tekst}'

    send_mail(
        f'Новый {instance.tekst}',
        f'НаВаше объявление новый отклик {instance.tekst}',
        f"{os.getenv('MY_MAIL')}",
        [f'{instance.user.email}'],
        fail_silently=False,
    )
    post_save.connect(check, sender=Response)
