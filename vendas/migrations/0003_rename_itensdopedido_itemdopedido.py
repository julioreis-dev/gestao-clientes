# Generated by Django 3.2.7 on 2021-09-07 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('vendas', '0002_remove_venda_telefone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItensDoPedido',
            new_name='ItemDoPedido',
        ),
    ]
