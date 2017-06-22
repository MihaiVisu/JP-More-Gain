from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=255)

class TeamCoder(models.Model):
    manager = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    memeber = models.ForeignKey(User, on_delete=models.CASCADE)

class Retrospective(models.Model):
    name = models.CharField(max_length=255)
    retroType = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Item(models.Model):
    POLL = 'PO'
    OPEN_QUESTION = 'OQ'
    SIMPLE_RATING = 'SR'
    QUESTION_TYPES = (
        (POLL, 'Poll'),
        (OPEN_QUESTION, 'Open_Question'),
        (SIMPLE_RATING, 'Simple_Rating')
    )
    name = models.CharField(max_length=255)
    itemType = models.CharField(max_length=2, choices=QUESTION_TYPES, default=OPEN_QUESTION)
    creationDate = models.DateField(null=True)
    retro = models.ForeignKey(Retrospective, on_delete=models.CASCADE)
    creator = models.ForeignKey(TeamCoder, on_delete=models.PROTECT)

class PollEntry(models.Model):
    entryText = models.CharField(max_length=255)
    suggestedBy = models.ForeignKey(TeamCoder, on_delete=models.PROTECT)
    entryQuestion = models.ForeignKey(Item, on_delete=models.CASCADE)

class Answer(models.Model):
    answerText = models.CharField(max_length=255)
    answerRating = models.IntegerField(default=3)
    authorUser = models.ForeignKey(TeamCoder, on_delete=models.PROTECT)
    answerQuestion = models.ForeignKey(Item, on_delete=models.CASCADE)
    answerPollEntry = models.ForeignKey(PollEntry, null=True, on_delete=models.SET_NULL)
