# Generated by Django 3.2.7 on 2021-09-07 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='telefone',
        ),
    ]
