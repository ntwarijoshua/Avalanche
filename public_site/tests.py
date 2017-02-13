from tenant_schemas.test.cases import TenantTestCase
from tenant_schemas.test.client import TenantClient
from django.core.urlresolvers import reverse
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


class TestTenantModel(CustomTenantTestCase):
	
	def setUp(self):
		self.c = TenantClient(self.tenant)

	def test_tenant_home(self):
		resp = self.c.get(reverse('tenant-home'))
		self.assertEquals(resp.status_code,200)

# class TestPublicSite(CustomTenantTestCase):
# 	def setUp(self):
# 		self.c = TenantClient(self.public_tenant)
# 	def test_public_home(self):
# 		resp = self.c.get(reverse('public-home'))
# 		self.assertEquals(resp.status_code,200)
		

