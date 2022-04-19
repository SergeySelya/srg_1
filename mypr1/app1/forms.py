from django import forms
from .models import Input


class InputForm(forms.Form):
    name0 = forms.CharField(label="")
    name0.widget.attrs['placeholder'] = "name0"
