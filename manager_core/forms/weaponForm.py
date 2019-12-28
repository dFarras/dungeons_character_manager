from django.forms import ModelForm
from manager_core.models import Weapon


class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields = '__all__'
