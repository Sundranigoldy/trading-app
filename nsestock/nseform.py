from django import forms
from .models import nsestock

class nsestockform(forms.ModelForm):
    class Meta:
        model = nsestock
        fields = ['nsesearch']