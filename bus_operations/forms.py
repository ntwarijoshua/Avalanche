from django import forms

class CreateRouteForm(forms.Form):
	route_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Route Name'}))
