from django.db import models

# Create your models here.
class Message(models.Model):
    message_text = models.CharField(max_length=1024)
