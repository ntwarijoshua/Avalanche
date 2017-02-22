from tenant_schemas.test.cases import TenantTestCase
from tenant_schemas.utils import get_tenant_model
from django.db import connection




class CustomTenantTestCase(TenantTestCase):
	@classmethod
	def setUpClass(cls):
		cls.sync_shared()
		tenant_domain = 'tenant.test.com'
		try:
			cls.tenant = get_tenant_model().objects.get(schema_name='test')
		except:
			cls.tenant = get_tenant_model()(domain_url=tenant_domain,schema_name='test',paid_until='2018-01-01',on_trial=False)
			cls.tenant.save(verbosity=0)
		connection.set_tenant(cls.tenant)
	

	@classmethod
	def tearDownClass(cls):
		connection.set_schema_to_public()
		#cls.tenant.delete()
		#cls.public_tenant.delete()