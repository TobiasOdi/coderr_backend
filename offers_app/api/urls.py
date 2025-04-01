from django.contrib import admin
from django.urls import path, include
from offers_app.api.views import ListAndCreateOffer, OfferDetailUpdateDelete
from profile_app.api.views import ProfileInfoView

urlpatterns = [
    path('', ListAndCreateOffer.as_view()),
    path('<int:offer_id>/', OfferDetailUpdateDelete.as_view())
]