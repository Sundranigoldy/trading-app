from .models import stock
from django import forms

class stockform(forms.ModelForm):
    class Meta:
        model = stock
        fields = ["search"]