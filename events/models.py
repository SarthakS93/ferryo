from django.db import models
from organizers.models import Organizer
# Create your models here.

class Event(models.Model):
	oganizer = models.ForeignKey(Organizer)
	type_id = models.IntegerField()
	picture = models.ImageField(upload_to = 'events')
	picture_width = models.SmallIntegerField()
	picture_height = models.SmallIntegerField()
	name = models.CharField(max_length = 100)
	description = models.TextField(max_length = 1000)
	place = models.TextField(max_length = 300)
	address = models.CharField(max_length = 100)
	zipcode = models.CharField(max_length = 6)
	city = models.CharField(max_length = 20)
	country = models.CharField(max_length = 20)
	lat_position   = models.DecimalField (max_digits = 10, decimal_places = 8)
	long_position   = models.DecimalField (max_digits = 10, decimal_places = 8)
	views = models.IntegerField(default = 0)
	date = models.DateTimeField()
	status = models.SmallIntegerField(default = 1)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)




# can add geoposition for storing lat-long
