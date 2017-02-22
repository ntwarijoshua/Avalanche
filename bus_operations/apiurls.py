from django.conf.urls import url
from bus_operations.apiviews import BusRoutesView,BusView

urlpatterns = [
    url(r'^buses$',BusView.as_view(),name='api-buses'),
    url(r'^buses/(?P<pk>\w+)$',BusView.as_view(),name='api-buses-params'),
    url(r'^bus-routes$',BusRoutesView.as_view(), name='api-bus-routes'),
    url(r'^bus-routes/(?P<pk>\w+)$',BusRoutesView.as_view(),name='api-bus-routes-params')
]