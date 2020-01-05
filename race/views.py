from django.shortcuts import render, HttpResponse
from race.models import Race, SubRace


# Create your views here.
def race(request):
    race_list = Race.objects.all
    return render(request, 'race.html', {'race_list': race_list})


def race_detail(request, race_name):
    race = Race.objects.get(name=race_name)
    race_imp = race.char_imp()
    return render(request, 'race_details.html', {'race': race, 'race_imp': race_imp})


def subrace_detail(request, race_name, subrace_name):
    race =  Race.objects.get(name=race_name)
    subrace = SubRace.objects.get(name=subrace_name)
    race_imp = race.char_imp()
    subrace_imp = subrace.char_imp()
    stat_impr = { k: race_imp.get(k, 0) + subrace_imp.get(k, 0) for k in set(race_imp) }
    return render(request, 'subrace_details.html', {'race': race_name, 'subrace': subrace, 'stat_impr': stat_impr})