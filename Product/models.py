from django.db import models
from django.contrib.auth.models import User


class ProductDetail(models.Model):
    option =(
        ("Tables and Chairs","Tables and Chairs"),
        ("Sleeping area and Childrens bedroom","Sleeping area and Childrens bedroom"),
        ("Sofas and Armchairs","Sofas and Armchairs")
    )
    Product_Id = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=255)
    Product_Brand = models.CharField(max_length=255)
    Product_Description = models.CharField(max_length=1000)
    Product_Price = models.IntegerField()
    Product_Category = models.CharField(max_length=255,choices=option)
    Product_Image = models.ImageField(upload_to="product_image")
    Product_Stock = models.CharField(max_length=255)
    Merchant = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
