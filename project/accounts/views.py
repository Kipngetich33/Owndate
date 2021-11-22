from django.shortcuts import render
from accounts.models import Account

# Create your views here.
def account_home(request):
    return render(request, 'account_home.html', {})


def accounts_index(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }
    return render(request, 'accounts_index.html', context)