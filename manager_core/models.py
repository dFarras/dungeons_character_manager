from django.db import models
from manager_core.dtos import WeaponType, DamageType


class Weapon(models.Model):
    name = models.CharField(max_length=128)
    #weaponType = models.CharField(
    #    max_length=5,
    #    choices=[(tag, tag.value()) for tag in WeaponType]
    #)
    price = models.PositiveIntegerField()
    #damage = models.ForeignKey(RollDice)
    #damageType = models.CharField(
    #    max_length=11,
    #    choices=[(tag, tag.value()) for tag in DamageType]
    #)
    weight = models.SmallIntegerField()
    properties = models.TextField()


class RollDice(models.Model):
    four = models.SmallIntegerField()
    six = models.SmallIntegerField()
    eight = models.SmallIntegerField()
    twelve = models.SmallIntegerField()
    twenty = models.SmallIntegerField()
