from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
	user = models.OneToOneField(User)
	role = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.user.username

class Team(models.Model):
    name = models.CharField(max_length=255)

class TeamUser(models.Model):
	team = models.ForeignKey(Team,on_delete=models.CASCADE)
	member = models.ForeignKey(Member,on_delete=models.CASCADE)
	manager = models.BooleanField()

class Retrospective(models.Model):
    name = models.CharField(max_length=255)
    retroType = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=255)
    itemType = models.CharField(max_length=255)
    retro = models.ForeignKey(Retrospective, on_delete=models.CASCADE)
    creator = models.ForeignKey(Member, on_delete=models.CASCADE)
