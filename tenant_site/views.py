from django.shortcuts import render,redirect
from general_management.forms import AuthForm
from invitation_manager.models import Invitation
from django.core.exceptions import ObjectDoesNotExist
from forms import AdminSetupForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.



def setup(request):
	if(request.GET.get('token') is not None):
	  	if(request.method == 'POST'):
		  	data = AdminSetupForm(request.POST)
		  	if(data.is_valid()):
		  		data.save(commit=True)
			  	Invitation.objects.get(invitation_token=request.GET.get('token')).delete()
			  	return redirect(index)
		else:	
		  	try:
			  Invitation.objects.get(invitation_token=request.GET.get('token'))
		  	except ObjectDoesNotExist:
			  tenant = request.tenant
			  message = 'Oops the token you submitted is invalid. contact administrator'
			  return render(request,'tenant_site/setup_exception.html',{'tenant':tenant,'message':message})
		  	form = AdminSetupForm()
		  	setup_token=request.GET.get('token')
		  	return render(request,'tenant_site/setup.html',{'form':form,'setup_token':setup_token})
	else:
		tenant = request.tenant
		message = 'Oops you need to submit a valid token on this url. contact administrator'
		return render(request,'tenant_site/setup_exception.html',{'tenant':tenant,'message':message})





def tenantAuth(request):
	if(request.method == 'POST'):
		data = AuthForm(request.POST)
		if data.is_valid():
			user = authenticate(username = data.cleaned_data['email'],password = data.cleaned_data['password'])
			if user is not None:
				login(request,user)
				if(request.GET.get('next') is not None):
					return redirect(request.GET.get('next'))
				else:
					return redirect(tenantDashboard)
			else:
				tenant = request.tenant
				return render(request,'tenant_site/login.html',{'form':data,'tenant':tenant,'login_message':'Invalid Credentials !'})
	else:
		form = AuthForm()
		tenant = request.tenant
		return render(request,'tenant_site/login.html',{'form':form,'tenant':tenant})

@login_required(login_url='/login/')
def tenantDashboard(request):
	return render(request,'tenant_site/dashboard.html')

def index(request):
	try:
		User.objects.get()
	except ObjectDoesNotExist:
		tenant = request.tenant
		message = 'Oops this tenant hasn\'t yet setup this domain. contact administrator'
		return render(request,'tenant_site/setup_exception.html',{'tenant':tenant,'message':message})
	return redirect(tenantAuth)

@login_required(login_url='/login/')
def logout_tenant(request):
	logout(request)
	return redirect(index)
	
