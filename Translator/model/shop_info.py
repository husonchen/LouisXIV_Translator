from django.db import models

class ShopInfo(models.Model):
    class Meta:
        db_table = 'shop_info'

    shop_id = models.IntegerField(primary_key=True)
    shop_name = models.CharField(max_length=255)
    shop_password = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    del_flag = models.BooleanField(default=0)
