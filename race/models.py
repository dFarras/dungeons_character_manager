from django.db import models


# Create your models here.
class CharImprovements(models.Model):
    stat = models.CharField(max_length=3)
    bonus = models.IntegerField()
    # import csv
    # with open('../tables/char_improvements.csv') as f:
    #    reader = csv.reader(f)
    #    for row in reader:
    #        created = CharImprovements(
    #            stat=row[0],
    #            bonus=int(row[1])
    #        )
    #        created.save()


class SubRace(models.Model):
    name = models.CharField(max_length=32, default='default')
    char_improvements = models.ManyToManyField(CharImprovements)
    # import csv
    # with open('../tables/Subraces.csv') as f:
    #    subrace = csv.reader(f)
    #    n = 1
    #    for sr in subrace:
    #        created = SubRace(name=sr[0])
    #        with open('../tables/subraces_has_char_improvements.csv') as g:
    #            for char in g:
    #                if int(char[0]) == n:
    #                    created.char_improvements.add(char[1])
    #        created.save()
    #    n += 1


class Race(models.Model):
    name = models.CharField(max_length=32, default='default')
    char_improvements = models.ManyToManyField(CharImprovements)
    #alignment = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    speed = models.IntegerField()
    sub_races = models.ForeignKey(SubRace, on_delete=models.CASCADE, blank=True, null=True)
    # import csv
    # with open('../tables/Races.csv') as f:
    #    reader = csv.reader(f)
    #    n = 1
    #    for r in reader:
    #        created = Race(
    #            name=r[0],
    #            speed=r[1],
    #            size=r[2]
    #        )
    #        with open('../tables/Races_has_Subraces.csv') as g:
    #            readerg = csv.reader(g)
    #            for l in readerg:
    #                if int(l[0]) == n:
    #                    print(n, l[0])
    #                    created.sub_races.add(l[1])
    #        with open('../tables/Races_has_char_improvements.csv') as h:
    #            readerh = csv.reader(h)
    #            for l in readerh:
    #                if int(l[0]) == n:
    #                    created.char_improvements.add(l[1])
    #        #created.save()
    #        n += 1
