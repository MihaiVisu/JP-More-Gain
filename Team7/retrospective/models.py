from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=255)

class TeamCoder(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    memeber = models.ForeignKey(User, on_delete=models.CASCADE)
    manager = models.BooleanField(default=False)

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
    itemType = models.CharField(max_length=255, choices=QUESTION_TYPES, default=OPEN_QUESTION)
    retro = models.ForeignKey(Retrospective, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creationDate = models.DateField(null=True)

class Answer(models.Model):
    answerText = models.CharField(max_length=255)
    answerRating = models.IntegerField()
    authorUser = models.ForeignKey(TeamCoder, on_delete=models.CASCADE)
    answerQuestion = models.ForeignKey(Item, on_delete=models.CASCADE)

class PollEntry(models.Model):
    entryText = models.CharField(max_length=255)
    suggestedBy = models.ForeignKey(TeamCoder, on_delete=models.CASCADE)
    entryQuestion = models.ForeignKey(Item, on_delete=models.CASCADE)