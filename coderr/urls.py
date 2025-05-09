"""
URL configuration for coderr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication_app.api.views import RegistrationView, LoginView, BaseInfoView
from profile_app.api.views import ProfileInfoView
from offers_app.api.views import OfferDetailItem
from orders_app.api.views import OrdersInProgress, OrdersCompleted

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/base-info/', BaseInfoView.as_view()),
    path('api/registration/', RegistrationView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/profile/', include('profile_app.api.urls')),    
    path('api/profiles/', include('profile_app.api.urls')),    
    path('api/reviews/', include('reviews_app.api.urls')),    
    path('api/offers/', include('offers_app.api.urls')),
    path('api/offerdetails/<int:pk>/', OfferDetailItem.as_view()),
    path('api/orders/', include('orders_app.api.urls')),
    path('api/order-count/<int:pk>/', OrdersInProgress.as_view()),     
    path('api/completed-order-count/<int:pk>/', OrdersCompleted.as_view())     
 
]
