from django.db import models


# Create your models here.
class Recibo(models.Model):
    year = models.IntegerField()
    quincena = models.IntegerField()
    fecha_pago = models.DateField()
    neto = models.DecimalField(max_digits=7, decimal_places=2)
    comentario = models.CharField(max_length=50)

    class Meta:
        ordering = ['year', 'quincena']