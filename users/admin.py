from django.contrib import admin
from .models import Profile, Users
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("image", "location", "phone")

class UsersAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "role", "recovered_on", "date_joined", "is_active")

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Users, UsersAdmin)