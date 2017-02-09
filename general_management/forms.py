from django import forms
from django.core.validators import RegexValidator


class AuthForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

class TenantsForm(forms.Form):
	validator= RegexValidator(r'^[a-z]+$','Only lowercased alphabetic character are allowed')
	domain = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Subdomain'}),validators=[validator])
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
	owner_email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Owner email'}))
		
