from avalanche.custom_testcase import CustomTenantTestCase
from tenant_schemas.test.client import TenantClient
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from .factories import BusFactory,BusRouteFactory
import json
import base64
# Create your tests here.


class TestBusOperationsEndPoints(CustomTenantTestCase):

	def setUp(self):
		admin = get_user_model().objects.create(
						username="test-admin",
						email="test@test.com",
						is_active=True,
						is_staff=True,
						is_superuser=True,
					)
		admin.set_password("testing")
		admin.save()
		self.c = TenantClient(self.tenant)
		self.auth_headers = {
			'HTTP_AUTHORIZATION':'Basic '+ base64.b64encode('test@test.com:testing'),
		}

	def test_getting_all_buses(self):
		resp = self.c.get(reverse('api-buses'),**self.auth_headers)
		self.assertEquals(resp.status_code,200)
	def test_creating_bus(self):
		resp = self.c.post(reverse('api-buses'),json.dumps({"number_plate":"RAC444D","passenger_seats":"50"}),content_type="application/json",**self.auth_headers)
		self.assertEquals(resp.status_code,200)
	def test_retrieving_a_bus(self):
		bus = BusFactory()
		bus.save()
		resp = self.c.get(reverse('api-buses-params', kwargs={'pk':bus.id}),**self.auth_headers)
		self.assertEquals(resp.status_code,200)
	def test_updating_a_bus(self):
		bus = BusFactory()
		bus.save()
		resp = self.c.put(reverse('api-buses-params',kwargs={'pk':bus.id}),json.dumps({"number_plate":"RAC455D"}),content_type="application/json",**self.auth_headers)
		self.assertEquals(resp.status_code,200)
	def test_deleting_a_bus(self):
		bus = BusFactory()
		bus.save()
		resp = self.c.delete(reverse('api-buses-params', kwargs={'pk':bus.id}),**self.auth_headers)
		self.assertEquals(resp.status_code,204)


	def test_getting_all_bus_routes(self):
		resp = self.c.get(reverse('api-bus-routes'),**self.auth_headers)
		self.assertEquals(resp.status_code,200)
	def test_creating_bus_routes(self):
		resp = self.c.post(reverse('api-bus-routes'),json.dumps({"name":"Remera-Mulindi-Kabuga"}),content_type="application/json",**self.auth_headers)
		self.assertEquals(resp.status_code,200)
	def test_retrieving_a_bus_routes(self):
		bus_route = BusRouteFactory()
		bus_route.save()
		resp = self.c.get(reverse('api-bus-routes-params', kwargs={'pk':bus_route.id}),**self.auth_headers)
		self.assertEquals(resp.status_code,200)
	def test_updating_a_bus_routes(self):
		bus_route = BusRouteFactory()
		bus_route.save()
		resp = self.c.put(reverse('api-bus-routes-params',kwargs={'pk':bus_route.id}),json.dumps({"name":"Remera-Mulindi-Masaka"}),content_type="application/json",**self.auth_headers)
		self.assertEquals(resp.status_code,200)
	def test_deleting_a_bus_routes(self):
		bus_route = BusRouteFactory()
		bus_route.save()
		resp = self.c.delete(reverse('api-bus-routes-params', kwargs={'pk':bus_route.id}),**self.auth_headers)
		self.assertEquals(resp.status_code,204)



