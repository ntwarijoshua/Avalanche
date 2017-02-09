import uuid
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from forms import AuthForm,TenantsForm
from tenants.models import Tenant
from invitation_manager.models import Invitation
from datetime import date,timedelta
from services import MailService
from exceptions import EmailNotSentException


def user_auth(request):

	if(request.method == 'POST'):
		data = AuthForm(request.POST)
		if data.is_valid():
			user = authenticate(username = data.cleaned_data['email'],password = data.cleaned_data['password'])
			if user is not None:
				login(request,user)
				if(request.GET.get('next') is not None):
					return redirect(request.GET.get('next'))
				else:
					return redirect(dashboard)
			else:
				return render(request,'general_management/login.html',{'form':data,'login_message':'Invalid Credentials !'})
	else:
		form = AuthForm()
		return render(request,'general_management/login.html',{'form':form})


@login_required
def dashboard(request):
	return render(request,'general_management/dashboard.html')

@login_required
def tenants_all(request):
	tenants = Tenant.objects.all()
	return render(request,'general_management/tenants-all.html',{'tenants':tenants})

@login_required
def create_tenants(request):
	if(request.method == 'POST'):
		data = TenantsForm(request.POST)
		if data.is_valid():
			#process and create tenant
			tenant_url = data.cleaned_data['domain']+'.'+'avalanche.dev' #TODO: this domain must be made dynamic not hardcoded
			company_name = data.cleaned_data['name']
			owner_email = data.cleaned_data['owner_email']
			tenant = Tenant(
					domain_url = tenant_url,
					schema_name= company_name.lower()+'schema',
					name=company_name,
					paid_until='2017-01-01', #TODO: come up with a payment scheme for tenants
					on_trial=True
				)
			invitation = Invitation(
						tenant_name=company_name,
						tenant_domain=tenant_url,
						invitation_expiration= date.today()+timedelta(days=2),
						invitation_token= uuid.uuid4().hex,
						invited_email = owner_email
				)
			

			# Emailing part
			try:
				invitation_url = tenant.domain_url+"/setup/?token="+invitation.invitation_token
				html = "<a href=\"%s\">click here to create administrator account</a>" % invitation_url
				mailer = MailService(recievers=["ntwarijoshua@gmail.com"],html=html)
				mailer.send()
			except EmailNotSentException:
				return redirect(tenants_all)
			tenant.save()
			invitation.save()
			return redirect(tenants_all)
			
		else:
			return render(request,'general_management/tenants-create.html',{'form':data})
	else:
		form = TenantsForm()
		return render(request,'general_management/tenants-create.html',{'form':form})

@login_required
def delete_tenants(request,pk):
	tenant = get_object_or_404(Tenant, pk=pk)
	tenant.delete()
	return redirect(tenants_all)


@login_required
def logout_user(request):
	logout(request)
	return redirect(user_auth)
