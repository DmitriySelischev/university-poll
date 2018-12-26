from django.db import models

__all__ = [
    'Identifiable',
    'Auditable'
]


# Create your models here.
class Identifiable(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        abstract = True


class Auditable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
