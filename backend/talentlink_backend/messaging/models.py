from django.db import models
from contracts.models import Contract
from users.models import User

class Message(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
