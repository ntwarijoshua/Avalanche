import factory
import models
class BusFactory(factory.Factory):
	class Meta:
		model = models.Bus

	number_plate = "RAC333V"
	passenger_seats = "50"

class BusRouteFactory(factory.Factory):
	class Meta:
		model = models.BusRoutes

	name = "Remera-Kicukiro-Ville"
		