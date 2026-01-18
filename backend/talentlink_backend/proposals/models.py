from django.db import models
from users.models import User
from projects.models import Project

class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    budget = models.IntegerField()
