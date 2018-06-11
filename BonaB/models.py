from django.db import models
from django.contrib.auth.models import User
import hashlib

# Create your models here.

class CryptoCurrency(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)
    currencyName = models.CharField(max_length=50)
    pszTimestamp = models.TextField(max_length=1024)
    maxMoney = models.CharField(max_length=30)
    halvingInterval = models.CharField(max_length=30)
    nDefaultPort = models.CharField(max_length=65535)
    nTime = models.CharField(max_length=30)
    nBits = models.CharField(max_length=40)
    nSubsidy = models.CharField(max_length=30)
    pubKey = models.CharField(max_length=1024)
    status = models.CharField(max_length=30)
    githubUser = models.CharField(max_length=50)
    githubPass = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    coinBase = models.CharField(max_length=30)
    currencyUnit = models.CharField(max_length=3)
    hashGenesisParams = models.CharField(max_length=40)
    owner = models.ForeignKey(User)
    downloadPassword = models.CharField(max_length=8)





class FullNode(models.Model) :
    address = models.CharField(max_length=45)
    cryptoCurrency = models.ForeignKey(CryptoCurrency)

class DnsSeed(models.Model) :
    domain = models.CharField(max_length=100)
    subDomain = models.CharField(max_length=20)
    cryptoCurrency = models.ForeignKey(CryptoCurrency)


class GenesisBlock(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)
    pszTimestamp = models.CharField(max_length=1024)
    coinBase = models.CharField(max_length=50)
    nBits = models.CharField(max_length=40)
    nNonce = models.CharField(max_length=50)
    mHash = models.CharField(max_length=200)
    nTime = models.CharField(max_length=30)
    pubKey = models.CharField(max_length=500)
    gHash = models.CharField(max_length=200)

    type = models.CharField(max_length=20)
    time = models.CharField(max_length=50)
    cryptoCurrency = models.ForeignKey(CryptoCurrency)

class Platform(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    aliasName = models.CharField(max_length=20)
    haveBuild = models.BooleanField(default=False)
    githubUrl = models.CharField(max_length=200)
    downloadUrl = models.CharField(max_length=200)
    hashCommit = models.CharField(max_length=40)
    repoStatus = models.IntegerField(default=0)
    buildStatus = models.IntegerField(default=0)
    cryptoCurrency = models.ForeignKey(CryptoCurrency)


