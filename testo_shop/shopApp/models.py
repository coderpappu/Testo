from django.db import models

# Create your models here.
class shopperProduct(models.Model):
    pro_name = models.CharField(max_length=30)
    pro_shopName = models.CharField(max_length=30, default="none")
    pro_desc = models.TextField(max_length=100)
    pro_price = models.IntegerField()
    pro_img = models.ImageField(upload_to='img/')
    pro_ID = models.CharField(max_length=20, unique=True)


class ShopperRegistration(models.Model):
    user_name = models.CharField(max_length=50, null=False)
    shop_name = models.CharField(max_length=100 ,null=False)
    user_mail = models.CharField(max_length=50, unique=True)
    user_mobile = models.CharField(max_length=12,unique=True)
    user_address = models.TextField(max_length=200)
    user_B_date= models.DateField()
    user_MBank = models.CharField(max_length=50)
    user_img = models.ImageField(upload_to='userImg',default='none')
    u_password = models.CharField(max_length=15, null=False, default='none')

class topProducts(models.Model):
    pro_name = models.CharField(max_length=30)
    pro_shopName = models.CharField(max_length=30, default="none")
    pro_desc = models.TextField(max_length=100)
    pro_price = models.IntegerField()
    pro_img = models.ImageField(upload_to='img/')
    pro_ID = models.CharField(max_length=20, unique=True)

class shopEvent(models.Model):
    Ev_name = models.CharField(max_length=100)
    Ev_desc = models.CharField(max_length=200)
    Ev_Img = models.ImageField(upload_to='event/')
    Ev_Date = models.DateField()

