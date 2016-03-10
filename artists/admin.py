from django.contrib import admin
from .models import Artist
# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'views', 'featured', 'awards', 'hirable']
	search_fields = ['user_id']
