from django.db import models
from account.models import MyUser
# Create your models here.

class Organizer(models.Model):
	user_id = models.ForeignKey(MyUser)
	picture = models.ImageField(upload_to = 'organizers/pics')
	description = models.TextField(max_length = 1000)
	owner = models.BooleanField(default = False)
	views = models.IntegerField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.user_id.first_name


class OrganizerSpecs(models.Model):
	Organizer = models.ForeignKey(Organizer)
	event_type_id = models.IntegerField()

	class Meta:
		verbose_name_plural = 'Organizer Specialties'

