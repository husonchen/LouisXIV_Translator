from django.db import models

class Settings(models.Model):
    class Meta:
        db_table = 'settings'

    id = models.IntegerField(primary_key=True)
    group = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

def getSetting(group,key):
    try:
        s = Settings.objects.get(group=group, key=key)
        return s.value
    except:
        return None
