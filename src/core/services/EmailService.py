from django.core.mail import send_mail
from django.conf import settings

from core.models import Answer

__all__ = [
    'EmailService'
]


class EmailService:
    def send_answer(self, answer: Answer):
        text = 'Name: {}\nUniversity: {}' \
            .format(answer.name, answer.university)
        send_mail('You answered', text, settings.EMAIL_FROM, [answer.email])
