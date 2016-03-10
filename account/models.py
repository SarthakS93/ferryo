from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
	phone = models.CharField(max_length = 10, null = True)	
	avatar = models.CharField(max_length = 255, default = '')
	phone = models.CharField(max_length = 10, null = True)
	status = models.SmallIntegerField(default = None)
	social_website = models.CharField(max_length = 100, default = '')
	social_facebook = models.CharField(max_length = 100, default = '')
	social_twitter = models.CharField(max_length = 100, default = '')
	social_google = models.CharField(max_length = 100, default = '')
	is_artist = models.BooleanField(default = False)
	is_organizer = models.BooleanField(default = False) 	
	price_currency_choices = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        ('INR', 'INR'), );
	preferences_currency = models.CharField(max_length = 3, choices = price_currency_choices, default = 'USD')
	size_choices = (
		('IN', 'IN'),
		('CM', 'CM')
	);
	preferences_unit = models.CharField(max_length = 2, choices = size_choices, default = 'IN')
	address = models.CharField(max_length = 100, default = '')
	zipcode = models.CharField(max_length = 6)
	city = models.CharField(max_length = 20, default = '')
	country = models.CharField(max_length = 20, default = '')
	lat_position = models.DecimalField(max_digits = 10, decimal_places = 8, null = True)
	long_position = models.DecimalField(max_digits = 10, decimal_places = 8, null = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	