from django.db import models
from artists.models import Artist
from account.models import MyUser
# Create your models here.

class Paintings(models.Model):
	artist_id = models.ForeignKey(Artist)
	category_id = models.IntegerField()
	picture = models.ImageField(upload_to = 'paintings')
	picture_width = models.SmallIntegerField()
	picture_height = models.SmallIntegerField()
	name = models.CharField(max_length = 255)
	description = models.TextField(max_length = 1000)
	materials = models.TextField(max_length = 1000)
	price = models.DecimalField (max_digits = 8, decimal_places = 2, null = True)
	price_currency_choices = (('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('INR', 'INR'));
	price_currency = models.CharField(max_length = 3, choices = price_currency_choices, default = 'USD')
	size_width = models.DecimalField(max_digits = 8, decimal_places = 2)
	size_height = models.DecimalField(max_digits = 8, decimal_places = 2)
	size_choices = (('IN', 'IN'), ('CM', 'CM'));
	size_unit = models.CharField(max_length = 2, choices = size_choices, default = 'IN')
	quantity = models.IntegerField()
	admin_message = models.TextField(max_length = 1000)
	views = models.IntegerField(default = 0)
	status = models.SmallIntegerField(default = 0)
	featured = models.BooleanField(default = False)
	featured_at = models.DateTimeField(blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Paintings'




class Likes(models.Model):
	painting_id = models.ForeignKey(Paintings)
	user_id = models.ForeignKey(MyUser)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name_plural = 'Likes'