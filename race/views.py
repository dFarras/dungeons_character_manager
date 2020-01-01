from django.shortcuts import render, HttpResponse
from race.models import Race, SubRace


# Create your views here.
def race(request):
    race_list = Race.objects.all
    return render(request, 'race.html', {'race_list': race_list})


def race_detail(request, race_name):
    race = Race.objects.get(name=race_name)
    return render(request, 'race_details.html', {'race': race})


def subrace_detail(request, race_name, subrace_name):
    subrace = SubRace.objects.get(name=subrace_name)
    return render(request, 'subrace_details.html', {'race': race_name, 'subrace': subrace})