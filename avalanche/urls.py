"""avalanche URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from tenant_site.views import index,setup,tenantDashboard,tenantAuth,logout_tenant

urlpatterns = [
	url(r'^$',index,name='tenant-home'),
	url(r'^setup/',setup,name='setup'),
	url(r'^login/',tenantAuth,name='tenant-auth'),
	url(r'^dashboard/',tenantDashboard,name='dashboard'),
	url(r'^logout/',logout_tenant,name='logout')
    
]+static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
