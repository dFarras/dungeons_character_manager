from django import forms
from manager_core.models import Weapon


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = '__all__'
