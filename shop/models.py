from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, default="")
    sub_category = models.CharField(max_length=20,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    desc = models.CharField(max_length=500)

    def __str__ (self):
        return self.product_name   


class Contact(models.Model):
    # Message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50 , default="")
    phone = models.CharField(max_length=50 ,default=0) 
    desc = models.CharField(max_length=1000,default="")

    def __str__ (self):
        return self.name    
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)

    def __str__ (self):
        return self.name    