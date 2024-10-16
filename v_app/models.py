
from django.db import models


# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_description = models.TextField()

    def __str__(self):
        return self.cat_name

class Product(models.Model):
    pro_name = models.CharField(max_length=50)
    pro_use = models.CharField(max_length=50)
    pro_cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    pro_price = models.CharField(max_length=20)
    pro_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.pro_name




class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(upload_to='contact', blank=True, null=True)

    def __str__(self):
        return self.subject

def get_default_category():
    default_category = Category.objects.get_or_create(name='Default Category')[0]
    return default_category.pk

class Order(models.Model):
    cus_name = models.CharField(max_length=50)
    cus_phone = models.CharField(max_length=12, blank=True, null=True)
    cus_email = models.EmailField()
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    pro_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.cus_name


class Medicines(models.Model):
    med_name = models.CharField(max_length=150)
    med_use = models.CharField(max_length=150)
    med_cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    med_price = models.CharField(max_length=20)
    med_image = models.ImageField(upload_to='medicines')

    def __str__(self):
        return self.med_name

class PharmLab(models.Model):
    test_name =  models.CharField(max_length=100)
    test_des = models.CharField(max_length=200)
    test_cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    test_price = models.CharField(max_length=20)
    test_image = models.ImageField(upload_to='pharmlab')

    def __str__(self):
        return self.test_name