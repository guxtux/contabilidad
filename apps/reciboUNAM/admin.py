from django.contrib import admin
from apps.reciboUNAM.models import Recibo
# Register your models here.

class ReciboAdmin(admin.ModelAdmin):
    model = Recibo
    list_display = ('year', 'quincena', 'fecha_pago')
    list_filter = ('year', 'quincena')
    ordering = ('-year',)

admin.site.register(Recibo, ReciboAdmin)
