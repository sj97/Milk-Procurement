from django.contrib.auth.models import User
from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class signUp(models.Model):
    CATEGORIES = (
        ('R', 'Receiver'),
        ('S', 'Supplier'),
    )
    category = models.CharField(max_length=3, choices=CATEGORIES)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField( max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique = True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    password = models.CharField(max_length=40)
    companyName = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200, default='N/A')

# class Receiver(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     shopName = models.CharField(max_length=100)
#     address = models.CharField(max_length=200, default='N/A')
#     # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
#     #                              message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     # contact = models.CharField(validators=[phone_regex], blank=True, max_length=15)  # validators should be a list
#     CATEGORIES = (
#         ('M', 'Milk'),
#         ('C', 'Cheese'),
#         ('O', 'Other'),
#     )
#     productType1 = models.CharField(max_length=3, choices=CATEGORIES)
#     quantity1 = models.IntegerField(default='0')
#
#
# class Supplier(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     companyName = models.CharField(max_length=100, default='')
#     address = models.CharField(max_length=200, default='N/A')
    # PERSONAL DETAILS
    # name = models.CharField(max_length=100, default='')
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # contact = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    #PRODUCT DETAILS
    # CATEGORIES = (
    #     ('M', 'Milk'),
    #     ('C', 'Cheese'),
    #     ('O', 'Other'),
    # )
    # productType1 = models.CharField(max_length=3, choices=CATEGORIES)
    # quantity1 = models.IntegerField(default='0')
    # expiryDate1 = models.DateField(default='2000-1-1')
    # productType2 = models.CharField(max_length=3, choices=CATEGORIES, blank=True)
    # quantity2 = models.IntegerField(default='0', blank=True)
    # expiryDate2 = models.DateField(default='2000-1-1', blank=True)


class ProductsAvailable(models.Model):
    location = models.CharField(max_length=30)
    supplier = models.EmailField(max_length=50)
    CATEGORIES = (
        ('C', 'CowMilk'),
        ('B', 'BuffaloMilk'),
        ('F', 'FullCream'),
        ('T', 'Toned'),
    )
    productType = models.CharField(max_length=3, choices=CATEGORIES)
    quantity = models.IntegerField()
    expiryDate = models.DateField(default='2000-01-01')
    expectedDelivery = models.DateField(default='2000-01-01')


#
# class ImmediateConsumers(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
#                                  message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     contact = models.CharField(validators=[phone_regex], blank=True, max_length=15)  # validators should be a list
#     adress = models.URLField(blank=True)
#     about = models.CharField(max_length=1000)
#
# class example (models.Model):
#     name = models.CharField(max_length=50)

