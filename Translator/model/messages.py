from django.db import models

class Messages(models.Model):
    translator_id = models.IntegerField()
    from_id = models.IntegerField()
    to_id = models.IntegerField()
    message_original = models.CharField