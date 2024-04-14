from django import forms
from .models import Car, Van, CampersCaravans


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner', )


class VanForm(forms.ModelForm):
    class Meta:
        model = Van
        exclude = ('owner', )


class CampersCaravansForm(forms.ModelForm):
    class Meta:
        model = CampersCaravans
        exclude = ('owner', )
