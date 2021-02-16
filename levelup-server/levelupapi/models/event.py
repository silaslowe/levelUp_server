from django.db import models


class Event(models.Model):

    event_day = models.DateField(auto_now=False, auto_now_add=False)
    event_time = models.TimeField(auto_now=False, auto_now_add=False)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    location = models.CharField(max_length=75)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
