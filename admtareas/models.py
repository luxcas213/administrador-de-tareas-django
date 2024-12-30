from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    importance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name +" - "+ self.user.username
    