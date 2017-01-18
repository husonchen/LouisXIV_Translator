from django.db import models

class TransMoney(models.Model):
    class Meta:
        db_table = 'trans_money'

    trans_id = models.IntegerField(primary_key=True)
    translator_id = models.IntegerField()
    last_translate_message_id = models.IntegerField()
    money_amount = models.IntegerField()
    alipay_account = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    del_flag = models.BooleanField(default=0)