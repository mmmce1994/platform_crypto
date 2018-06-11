from BonaB.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class CryptoCurrencySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = CryptoCurrency
        fields = ('id',  'owner' , 'pszTimestamp', 'maxMoney', 'halvingInterval', 'nDefaultPort', 'nTime', 'nBits', 'dnsSeed', 'nSubsidy' ,'status', 'hashGenesisParams')


class FullNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FullNode
        fields = ('id', 'address', 'cryptoCurrency')

class DnsSeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DnsSeed
        fields = ('id', 'subDomain', 'domain', 'cryptoCurrency')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id' , 'url', 'username', 'email', 'groups', 'cryptocurrencies')