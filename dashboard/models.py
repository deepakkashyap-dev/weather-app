from django.db import models
from django.contrib.auth.models import User

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255,null=True)
    desc = models.CharField(max_length=255,null=True)
    temperature = models.CharField(max_length=255,null=True)
    humidity = models.CharField(max_length=255,null=True)
    icon = models.CharField(max_length=255,null=True)
    wind = models.CharField(max_length=255,null=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} searched for "{self.city}"'

