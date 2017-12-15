from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index_factura(request):
    return HttpResponse('Index - Mensaje desde la vista en factura')
