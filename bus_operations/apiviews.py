from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from models import BusRoutes,Bus
from serializers import BusSerializer,BusRoutesSerializer
from rest_framework.permissions import IsAuthenticated





class BusRoutesView(APIView):
		def get(self,request, pk=None):
			if(pk is not None):
				try:
					bus_route = BusRoutes.objects.get(pk=pk)
				except BusRoutes.DoesNotExist:
					return HttpResponse(status=404)
				else:
					serialized = BusRoutesSerializer(bus_route)
					return Response(serialized.data)
			else:
				bus_routes = BusRoutes.objects.all()
				serialized = BusRoutesSerializer(bus_routes,many=True)
				return Response(serialized.data)

		def post(self,request):
			data = JSONParser().parse(request)
			serialized = BusRoutesSerializer(data=data)
			if serialized.is_valid():
				serialized.save()
				return Response(serialized.data)
			else:
				return Response(serialized.errors)

		def put(self,request,pk=None):
			data = JSONParser().parse(request)
			try:
				bus_route = BusRoutes.objects.get(pk=pk)
			except BusRoutes.DoesNotExist:
				return HttpResponse(status=404)
			else:
				serialized = BusRoutesSerializer(instance=bus_route,data=data)
				if serialized.is_valid():
					serialized.save()
					return Response(serialized.data)
				else:
					return Response(serialized.errors)

		def delete(self,request,pk=None):
			try:
				bus_route = BusRoutes.objects.get(pk=pk)
			except BusRoutes.DoesNotExist:
				return HttpResponse(status=404)
			else:
				bus_route.delete()
				return HttpResponse(status=204)
		


class BusView(APIView):
		permission_classes=(IsAuthenticated,)
		def get(self,request, pk=None):
			if(pk is not None):
				try:
					bus = Bus.objects.get(pk=pk)
				except Bus.DoesNotExist:
					return HttpResponse(status=404)
				else:
					serialized = BusSerializer(bus)
					return Response(serialized.data)
			else:
				buses = Bus.objects.all()
				serialized = BusSerializer(buses,many=True)
				return Response(serialized.data)


		def post(self,request):
			data = JSONParser().parse(request)
			serialized = BusSerializer(data=data)
			if serialized.is_valid():
				serialized.save()
				return Response(serialized.data)
			else:
				return Response(serialized.errors)


		def put(self,request,pk=None):
			data = JSONParser().parse(request)
			try:
				bus = Bus.objects.get(pk=pk)
			except Bus.DoesNotExist:
				return HttpResponse(status=404)
			else:
				serialized = BusSerializer(instance=bus,data=data)
				if serialized.is_valid():
					serialized.save()
					return Response(serialized.data)
				else:
					return Response(serialized.errors)


		def delete(self,request,pk=None):
			try:
				bus = Bus.objects.get(pk=pk)
			except Bus.DoesNotExist:
				return HttpResponse(status=404)
			else:
				bus.delete()
				return HttpResponse(status=204)
			