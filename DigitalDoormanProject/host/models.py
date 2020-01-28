from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Event(models.Model):
    hostUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
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