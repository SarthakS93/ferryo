from django.db import models
from account.models import MyUser

# Create your models here.

class Artist(models.Model):
	user_id = models.ForeignKey(MyUser)
	picture = models.ImageField(upload_to = 'artists/pics')	
	bio = models.TextField(max_length = 1000)
	awards = models.CharField(max_length = 200)	
	hirable = models.BooleanField(default = False)
	views = models.IntegerField(default = 0)
	featured = models.SmallIntegerField(default = 0)
	featured_at = models.DateTimeField(blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.user_id.first_name

class ArtistSkill(models.Model):
	artist_id = models.ForeignKey(Artist)
	category_id = models.IntegerField()

	
	



