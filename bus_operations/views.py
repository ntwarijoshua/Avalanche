from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView
from forms import CreateRouteForm
from models import BusRoutes
# Create your views here.



class BusListRoutesView(TemplateView):
	template_name = 'bus_operations/list.html'
	def get_context_data(self, **kwargs):
	    context = super(BusListRoutesView, self).get_context_data(**kwargs)
	    context['routes'] = BusRoutes.objects.all()
	    return context

class BusCreateRoutesView(View):
	
	def get(self,request):
		form = CreateRouteForm()
		return render(request,'bus_operations/create.html',{'form':form})

	def post(self,request):
		data = CreateRouteForm(request.POST)
		if data.is_valid():
			route = BusRoutes(name=data.cleaned_data['route_name'])
			route.save()
			return redirect('list-routes')
		else:
			return render(request,'bus_operations/create.html',{'form':data})

