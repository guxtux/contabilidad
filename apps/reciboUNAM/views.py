from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.reciboUNAM.forms import ReciboForm
from apps.reciboUNAM.models import Recibo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Para las vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

# Para serializar objetos
from django.core import serializers

#usando el restframework
from rest_framework.views import APIView
from apps.reciboUNAM.serializers import ReciboSerializer
import json


def listado(request):
    lista = serializers.serialize('json', Recibo.objects.all())
    return HttpResponse(lista, content_type='application/json')

# Create your views here.




def index(request):
    # return HttpResponse('Index - Mensaje desde la vista en reciboUNAM')
    return render(request, 'recibos/index.html')


def recibo_view(request):
    if request.method == 'POST':
        form = ReciboForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('recibos:index')
    else:
        form = ReciboForm()

    return render(request, 'recibos/recibo_form.html', {'form': form})


def recibo_list(request):
    recibo = Recibo.objects.all()
    contexto = {'recibos': recibo}
    return render(request, 'recibos/recibo_list.html', contexto)


def recibo_edit(request, id_recibo):
    recibo = Recibo.objects.get(id=id_recibo)
    if request.method == 'GET':
        form = ReciboForm(instance=recibo)
    else:
        form = ReciboForm(request.POST, instance=recibo)
        if form.is_valid():
            form.save()
        return redirect('recibos:recibo_listar')
    return render(request, 'recibos/recibo_form.html', {'form': form})


def recibo_delete(request, id_recibo):
    recibo = Recibo.objects.get(id=id_recibo)
    if request.method == 'POST':
        recibo.delete()
        return redirect('recibos:recibo_listar')
    return render(request, 'recibos/recibo_delete.html', {'recibos': recibo})

# Vistas basadas en clases:

class ReciboList(ListView):
    model = Recibo
    template_name = 'recibos/recibo_list.html'
    paginate_by = 10


def recibo_listing(request):
    recibo_list = Recibo.objects.all()
    paginator = Paginator(recibo_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    recibos = paginator.get_page(page)
    return render(request, 'recibos/recibo_list.html', {'recibos': recibos})

class ReciboCreate(CreateView):
    model = Recibo
    form_class = ReciboForm
    template_name = 'recibos/recibo_form.html'
    success_url = reverse_lazy('recibos:recibo_listar')


class ReciboUpdate(UpdateView):
    model = Recibo
    form_class = ReciboForm
    template_name = 'recibos/recibo_form.html'
    success_url = reverse_lazy('recibos:recibo_listar')


class ReciboDelete(DeleteView):
    model = Recibo
    template_name = 'recibos/recibo_delete.html'
    success_url = reverse_lazy('recibos:recibo_listar')


class ReciboAPI(APIView):
    serializer = ReciboSerializer

    def get(self, request, format=None):
        lista = Recibo.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')


class ReciboYear(ListView):
   model = Recibo
   template_name = 'recibos/recibo_year.html'
   paginate_by = 10

   # Modifying the get_context_data method

   def get_queryset(self):
       queryset = Recibo.objects.all()
       if self.request.GET.get("year"):
           selection = self.request.GET.get("year")
           if selection == "2017":
               queryset = Recibo.objects.filter(year=2017)
           elif selection == "2016":
               queryset = Recibo.objects.filter(year=2016)
           elif selection == "2015":
               queryset = Recibo.objects.filter(year=2015)
           elif selection == "2014":
               queryset = Recibo.objects.filter(year=2014)
           else:
               queryset = Recibo.objects.all()
       return queryset
