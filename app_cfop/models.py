from django.db import models

# Create your models here.
class CfopEntrada(models.Model):
  cfop_com = models.CharField(max_length=4)
  nome = models.CharField(max_length=70)
  id_compra = models.ForeignKey('self', on_delete=models.CASCADE)


class CfopCompra(models.Model):
  id = models.AutoField(primary_key=True)
  cfop_com = models.CharField(max_length=4, null=False)
  nome = models.CharField(max_length=70)