from django.contrib import admin
from .models import Organizer, OrganizerSpecs
# Register your models here.

class OrganizerAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'description', 'views']
	search_fields = ['user_id']

class OrganizerSpecsAdmin(admin.ModelAdmin):
	list_display = ['Organizer', 'event_type_id']
	search_fields = ['Organizer']

admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(OrganizerSpecs, OrganizerSpecsAdmin)