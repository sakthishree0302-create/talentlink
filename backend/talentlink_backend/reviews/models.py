from django.db import models
from contracts.models import Contract
from users.models import User

class Review(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
