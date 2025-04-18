from django.contrib import admin
from django.urls import path, include
from orders_app.api.views import ListAndCreateOrders

urlpatterns = [
    path('', ListAndCreateOrders.as_view()),
]