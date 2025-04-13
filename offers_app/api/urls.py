from django.contrib import admin
from django.urls import path, include
from offers_app.api.views import ListAndCreateOffer, OfferDetailUpdateDelete, ListDetails
from profile_app.api.views import ProfileInfoView

urlpatterns = [
    path('', ListAndCreateOffer.as_view()),
    path('<int:pk>/', OfferDetailUpdateDelete.as_view(), name="details-detail"),
    path('<int:pk>/details/', ListDetails.as_view(), name="details-detail")
    
]