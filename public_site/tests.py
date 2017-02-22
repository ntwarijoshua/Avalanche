from avalanche.custom_testcase import CustomTenantTestCase
from tenant_schemas.test.client import TenantClient
from django.core.urlresolvers import reverse

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
		

