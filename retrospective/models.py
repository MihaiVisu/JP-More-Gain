from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=255)

class TeamCoders(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    memeber = models.ForeignKey(User,on_delete=models.CASCADE)
    manager = models.BooleanField(default=False)

class Retrospective(models.Model):
    name = models.CharField(max_length=255)
    retroType = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=255)
    itemType = models.CharField(max_length=255)
    retro = models.ForeignKey(Retrospective, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creationDate = models.DateField(null=True)