from django.db import models
from users.models import User

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.CharField(max_length=200)
    budget = models.IntegerField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)
