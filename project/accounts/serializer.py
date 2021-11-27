from accounts.models import Account
from rest_framework import serializers, viewsets

# Serializers define the API representation.
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['pk','user_name','email', 'phone_number','bio']

# ViewSets define the view behavior.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer