from django import forms

class CCGForm(forms.Form):

    currencyName = forms.RegexField(max_length=30, required=True, regex="^[a-zA-Z][a-zA-Z0-9]+$")
    pszTimestamp = forms.TextField(max_length=1024, required=True)
    maxMoney = forms.CharField(max_length=30)
    halvingInterval = forms.IntegerField(required=True)
    nDefaultPort = forms.IntegerField(max_value=65535, required=True, min_length=1024)
    nTime = forms.CharField(max_length=30, required=True)
    nBits = forms.CharField(max_length=40)
    nSubsidy = forms.CharField(max_length=30)
    pubKey = forms.CharField(max_length=130, min_length=130)
    githubUser = forms.CharField(max_length=50, required=True)
    githubPass = forms.CharField(max_length=50, required=True)
    coinBase = forms.CharField(max_length=maxMoney, required=True)
    currencyUnit = forms.CharField(max_length=3, required=True)




