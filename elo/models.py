from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=25)
    current_elo = models.IntegerField(default=800)

    def __str__(self):
        return self.name


class Game(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    winner = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='won_games')
    loser = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='lost_games')
    winner_elo_before = models.FloatField()
    winner_elo_after = models.FloatField()
    loser_elo_before = models.FloatField()
    loser_elo_after = models.FloatField()
