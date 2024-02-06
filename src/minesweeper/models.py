from django.db import models


class Game(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    mines_count = models.IntegerField()
    field = models.JSONField(default=list)
    completed = models.BooleanField(default=False)
