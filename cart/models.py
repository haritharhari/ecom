from django.db import models 
from Product.models import ProductDetail
from django.contrib.auth.models import User

class cart(models.Model):
    product = models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
    numberofitems = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # date = models.DateTimeField()
    status = models.BooleanField(default=False)

class PurchasedItems(models.Model):
    product = models.ForeignKey(ProductDetail,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    paymentstatus = models.BooleanField(default=False)
    