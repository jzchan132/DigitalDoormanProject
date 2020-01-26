from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    eventID = models.IntegerField()
    event_slug = models.CharField(max_length=200, default=1)

    class meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title

class Guest(models.Model):
    inEvent = models.ForeignKey(Event,db_index=True, verbose_name="Events", on_delete=models.CASCADE)
    qrID = models.IntegerField()
    tokens = models.IntegerField()