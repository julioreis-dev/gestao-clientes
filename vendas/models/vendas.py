from django.db import models
from django.db.models import Sum, F, FloatField
from produtos.models.produtos import Produto
from django.core.mail import send_mail, mail_admins, send_mass_mail
from django.template.loader import render_to_string
from clientes.models import Person


class Venda(models.Model):
    numero = models.CharField(max_length=30)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    impostos = models.DecimalField(max_digits=5, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    nfe_emitida = models.BooleanField(default=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # produtos = models.ManyToManyField(Produto, Blank=True)
    # telefone = models.CharField(max_length=20, null=True, blank=True)

    def get_total(self):
        tot = self.itemdopedido_set.all().aggregate(
            tot_ped=Sum(F('quantidade') * F('produto__preco'), output_field=FloatField())
        )['tot_ped'] or None
        return tot

    def __str__(self):
        return self.numero


class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return str(self.venda)
