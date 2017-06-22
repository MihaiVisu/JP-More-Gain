from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)

class Coder(models.Model):
	user = models.OneToOneField(User)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	manager = models.BooleanField()

	def __unicode__(self):
		return self.user.username

class Retrospective(models.Model):
    name = models.CharField(max_length=255)
    retroType = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=255)
    itemType = models.CharField(max_length=255)
    retro = models.ForeignKey(Retrospective, on_delete=models.CASCADE)
    creator = models.ForeignKey(Coder, on_delete=models.CASCADE)
    creationDate = models.DateField()