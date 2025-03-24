from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('registration/', admin.site.urls),
]