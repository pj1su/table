from django import forms
from . import models


class ListForm(forms.ModelForm):
    class Meta:
        model = models.ListModel
        fields = ("title", "description", "host")
