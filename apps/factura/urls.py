from django.urls import path

#codigo equivalente
#from apps.reciboUNAM.views import index
#path(r'^$', index)
from apps.factura.views import index_factura

urlpatterns = [
    path('', index_factura, name='indexfactura'),
]