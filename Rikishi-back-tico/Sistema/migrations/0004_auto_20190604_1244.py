# Generated by Django 2.1.2 on 2019-06-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0003_auto_20190603_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_pedido',
            name='precio',
            field=models.IntegerField(blank=True, max_length=6),
        ),
    ]