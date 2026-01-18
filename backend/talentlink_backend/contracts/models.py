from django.db import models
from proposals.models import Proposal

class Contract(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='active')
