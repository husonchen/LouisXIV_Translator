from django.db import models

class TranslatorUser(models.Model):
    class Meta:
        db_table = 'translator_user'
    translator_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255)
    mail_address = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    alipay_account = models.CharField(max_length=255,default='')
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    del_flag = models.BooleanField(default=0)
