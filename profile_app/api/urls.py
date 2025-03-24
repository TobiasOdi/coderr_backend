from django.contrib import admin
from django.urls import path, include
from authentication_app.api.views import RegistrationView, LoginView
from profile_app.api.views import ProfileInfoView

urlpatterns = [
    path('<int:user_id>/', ProfileInfoView.as_view()),
    # path('/business/', ProfileInfoView.as_view()),
    # path('/customer/', ProfileInfoView.as_view()),

]