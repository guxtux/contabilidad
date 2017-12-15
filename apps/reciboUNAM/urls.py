from django.urls import path

#codigo equivalente

import apps.reciboUNAM.views

#path(r'^$', index)
#from . import views

app_name = 'recibos'

urlpatterns = [
    path('', apps.reciboUNAM.views.index, name='index'),
    path('nuevo/', apps.reciboUNAM.views.recibo_view, name='recibo_nuevo'),
    path('listar/', apps.reciboUNAM.views.recibo_list, name='recibo_listar'),
    path('editar/<id_recibo>/', apps.reciboUNAM.views.recibo_edit, name='recibo_editar'),
    path('eliminar/<id_recibo>/', apps.reciboUNAM.views.recibo_delete, name='recibo_eliminar'),
]