from django.contrib import admin
from reviews_app.models import Review
class ReviewAdmin(admin.ModelAdmin):
    fields    = "__all__"

admin.site.register(Review)
