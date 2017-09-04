from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Message(models.Model):
    message_text = models.CharField(max_length=1024)

    def __str__(self):
        return self.message_text
