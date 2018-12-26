from django.db import models
from django.utils.translation import ugettext_lazy as _

from .common import Auditable, Identifiable

__all__ = [
    'Answer'
]


class Answer(Auditable, Identifiable):
    UNIVERSITY_CHOICES = (
        ('KNTU', _('KNTU')),
        ('KSU', _('KSU')),
        ('KSAU', _('KSAU')),
        ('KMA', _('KMA')),
    )

    email = models.EmailField()
    name = models.CharField(max_length=255)
    university = models.CharField(max_length=255, choices=UNIVERSITY_CHOICES)
