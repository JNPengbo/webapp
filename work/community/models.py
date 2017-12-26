from django.db import models

# Create your models here.
class user_info(models.Model):
    user_name = models.CharField(max_length=24)
    user_password = models.CharField(max_length=60)
    user_nickname = models.CharField(max_length=24)
    user_createtime = models.DateTimeField(auto_now_add=True)
