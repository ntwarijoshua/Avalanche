
from django.conf.urls import url
from general_management.views import user_auth,dashboard,logout_user,tenants_all,create_tenants,delete_tenants
from django.conf import settings
from django.conf.urls.static import static
from public_site.views import index


urlpatterns = [
    url(r'^admin/', user_auth, name='login'),
    url(r'^logout/',logout_user, name='logout'),
    url(r'^dashboard/',dashboard, name='dashboard'),
    url(r'^tenants/create/',create_tenants, name='create-tenants'),
    url(r'^tenants/delete/(?P<pk>\d+)$',delete_tenants, name='delete-tenants'),
    url(r'^tenants/',tenants_all, name='list-tenants'),
    url(r'^$',index)
]+static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)