from __future__ import unicode_literals

from django.db import models
from tenant_schemas.models import TenantMixin

class Tenant(TenantMixin):
	name = models.CharField(max_length=100)
	paid_until = models.DateField()
	on_trial = models.BooleanField()
	created_on = models.DateField(auto_now_add=True)
	auto_create_schema = True
	auto_drop_schema = True


# tenant = Tenant(
# 	domain_url='127.0.0.1:8000', # don't add your port or www here! on a local server you'll want to use localhost here
#     schema_name='public',
#     name='Schemas Inc.',
#     paid_until='2016-12-05',
#     on_trial=False
#     )
# tenant.save()
	
