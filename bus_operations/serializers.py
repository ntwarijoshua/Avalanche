from rest_framework import serializers
from models import Bus,BusRoutes

class BusSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	number_plate = serializers.CharField(max_length=7)
	passenger_seats = serializers.IntegerField()

	def create(self,validated_data):
		return Bus.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.number_plate = validated_data.get('number_plate',instance.number_plate)
		instance.passenger_seats = validated_data.get('passenger_seats',instance.passenger_seats)
		instance.save()
		return instance

class BusRoutesSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	name = serializers.CharField(max_length=100)

	def create(self,validated_data):
		return BusRoutes.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.name = validated_data.get('name',instance.name)
		instance.save()
		return instance


		
