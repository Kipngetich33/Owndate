#other application imports
from django.urls import path,include
from rest_framework import routers

#application level import
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', views.account_home, name='account_home'),
    path('accounts/<int:pk>/', views.account_details, name='account_details'),
]

