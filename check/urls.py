"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('car_check/', views.Car_checkView.as_view(), name='car_check'),
    path('car_delivery/', views.Car_deliveryView.as_view(), name='car_delivery'),
    path('car_confirm/', views.Car_confirmView.as_view(), name='car_confirm'),




]
