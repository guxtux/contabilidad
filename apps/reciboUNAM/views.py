from django.shortcuts import render, redirect
#from django.http import HttpResponse
from apps.reciboUNAM.forms import ReciboForm
from apps.reciboUNAM.models import Recibo

# Para las vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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


