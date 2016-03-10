from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display = ['name', 'orgainzer', 'type_id', 'city']
	search_fields = ['name']

admin.site.register(Event)
