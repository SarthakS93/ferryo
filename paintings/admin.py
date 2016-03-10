from django.contrib import admin
from .models import Paintings, Likes
# Register your models here.

class PaintingsAdmin(admin.ModelAdmin):
	list_display = ['name', 'artist_id', 'category_id', 'price']
	search_fields = ['name']

class LikesAdmin(admin.ModelAdmin):
	list_display = ['painting_id', 'user_id']
	search_fields = ['painting_id']

admin.site.register(Paintings, PaintingsAdmin)
admin.site.register(Likes, LikesAdmin)
	




