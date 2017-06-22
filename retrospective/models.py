from django.db import models

class Retrospective(models.Model):
    name = models.CharField()
    type = models.CharField()
    owner = models.ForeignKey(Team, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField()
    type = models.CharField()
    retro = models.ForeignKey(Retrospective, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class User(models.Model):
    fst_name = CharField()
    last_name = CharField()
    role = CharField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Team(models.Model):
    name = CharFIeld()
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

