from django.contrib import admin
from profile_app.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields    = "__all__"

admin.site.register(Profile)
