from django.db import models

class TranslateMessages(models.Model):
    class Meta:
        db_table = 'translate_messages'

    message_id = models.IntegerField(primary_key=True)
    shop_id = models.IntegerField()
    custom_id = models.IntegerField()
    custom_name = models.CharField(max_length=255)
    message_original = models.CharField(max_length=1024)
    message_translate = models.CharField(max_length=1024)
    translator_id = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    del_flag = models.BooleanField(default=0)
    sr_flag = models.BooleanField(default=0)
