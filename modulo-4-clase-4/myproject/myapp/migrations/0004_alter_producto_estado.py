# Generated by Django 5.1.3 on 2024-11-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_producto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[(1, 'DISPONIBLE'), (0, 'AGOTADO')], default='DISPONIBLE', max_length=10),
        ),
    ]
