from django.contrib import admin
from django.urls import path, include
from offers_app.api.views import ListAndCreateOffer, OfferDetailUpdateDelete, OfferDetailItem
from profile_app.api.views import ProfileInfoView

urlpatterns = [
    path('', ListAndCreateOffer.as_view(), name="details-list"),
    path('<int:pk>/', OfferDetailUpdateDelete.as_view(), name="details-list")
]