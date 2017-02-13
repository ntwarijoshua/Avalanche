from django.contrib.auth.forms import UserCreationForm
from django import forms


class AdminSetupForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput({'class':'form-control','placeholder':'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput({'class':'form-control','placeholder':'Last Name'}))
	username = forms.CharField(widget=forms.TextInput({'class':'form-control','placeholder':'Username'}))
	email = forms.EmailField(widget=forms.EmailInput({'class':'form-control','placeholder':'Email'}))
	password1 = forms.CharField(label='Password',widget=forms.PasswordInput({'class':'form-control','placeholder':'Password'}))
	password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput({'class':'form-control','placeholder':'Confirm Password'}))


	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.first_name=self.cleaned_data["first_name"]
		user.last_name=self.cleaned_data["last_name"]
		user.username=self.cleaned_data["username"]
		user.email=self.cleaned_data["email"]
		user.is_superuser=True
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user	
