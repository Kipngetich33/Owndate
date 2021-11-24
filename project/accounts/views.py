from django.shortcuts import render
from accounts.models import Account

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def account_home(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts
    }
    return render(request, 'account_home.html', context)


def account_details(request,pk):
    account = Account.objects.get(pk=pk)
    context = {
        'account': account
    }
    return render(request, 'account_details.html', context)