from django.contrib import admin
from .models import MyUser
# Register your models here.

@admin.register(MyUser)
class ActiveUserAdmin(admin.ModelAdmin):
	list_display = ['username', 'is_superuser', 'is_artist', 'is_organizer', 'city']
	search_fields = ['username']
