from django.db import models
from accounts.models import Person


class Message(models.Model):
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='receiver')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_modified = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now=True)
