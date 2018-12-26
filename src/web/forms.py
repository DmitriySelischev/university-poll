from django import forms
from django.utils.translation import ugettext_lazy as _
from core.models import Answer

__all__ = [
    'AnswerForm'
]


# Create your forms here
class AnswerForm(forms.Form):
    email = forms.EmailField(label=_('Email'),
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=255, label=_('Name'),
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    university = forms.ChoiceField(label=_('University'),
                                   choices=Answer.UNIVERSITY_CHOICES,
                                   widget=forms.Select(attrs={'class': 'form-control'}))
