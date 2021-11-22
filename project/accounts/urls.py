from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.account_home, name='account_home'),
    path('accounts_index', views.accounts_index, name='accounts_index'),
]

