from django.db import models


# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=32, default='default')
    size = models.CharField(max_length=20)
    speed = models.IntegerField()
    #alignment = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    # import csv
    # with open('../tables/Races.csv') as f:
    #    reader = csv.reader(f)
    #    for r in reader:
    #        created = Race(
    #            name=r[0],
    #            speed=r[1],
    #            size=r[2]
    #        )
    #        created.save()



class SubRace(models.Model):
    name = models.CharField(max_length=32, default='default')
    race = models.ForeignKey(Race, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    # import csv
    # with open('../tables/Subraces.csv') as f:
    #     readerf = csv.reader(f)
    #     n = 1
    #     for subrace in readerf:
    #         with open('../tables/Races_has_Subraces.csv') as g:
    #             readerg = csv.reader(g)
    #             for l in readerg:
    #                if int(l[1]) == n:
    #                    created = SubRace(name=subrace[0],
    #                                      race=Race.objects.get(pk=int(l[0]))
    #                                      )
    #         created.save()
    #         n += 1


class CharImprovements(models.Model):
    stat = models.CharField(max_length=3)
    bonus = models.IntegerField()
    race = models.ManyToManyField(Race)
    subrace = models.ManyToManyField(SubRace)
    # with open('../tables/char_improvements.csv') as f:
    #     reader = csv.reader(f)
    #     n=1
    #     for row in reader:
    #         created = CharImprovements(
    #             stat=row[0],
    #             bonus=int(row[1])
    #         )
    #         created.save()
    #         with open('../tables/Races_has_char_improvements.csv') as g:
    #             readerg = csv.reader(g)
    #             for rowg in readerg:
    #                 if int(rowg[1]) == n:
    #                     created.race.add(Race.objects.get(pk=int(rowg[0])))
    #         with open('../tables/Subraces_has_char_improvements.csv') as h:
    #             readerh = csv.reader(h)
    #             for rowh in readerh:
    #                 if int(rowh[1]) == n:
    #                     created.subrace.add(SubRace.objects.get(pk=int(rowh[0])))
    #         created.save()
    #         n += 1