from django.shortcuts import render
from django.http import HttpResponse
from manager_core.forms.weaponForm import WeaponForm


def index(request):
    return HttpResponse("This view is intended to show characters sheet.")


def weapons(request):
    form = WeaponForm()
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            weapon = form.save(commit=False)
            weapon.save()
    else:
        form = WeaponForm()
        return render(request, 'weaponTemplate.html', {'form': form})
