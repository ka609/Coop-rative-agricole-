# Generated by Django 5.1.1 on 2024-11-15 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestions', '0009_productionagricole_delete_production'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default='<function uuid4 at 0x0000018E90CA8A40>', max_length=255, unique=True),
        ),
    ]
