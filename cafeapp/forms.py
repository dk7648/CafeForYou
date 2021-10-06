from django import forms
from django.forms import ModelForm

from cafeapp.models import Cafe


class CafeCreationForm(ModelForm):
    class Meta:
        model = Cafe
        fields = ['name', 'content']