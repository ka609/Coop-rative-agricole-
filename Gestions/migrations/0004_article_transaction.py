# Generated by Django 5.1.1 on 2024-11-03 14:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestions', '0003_membre_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('vendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_vendus', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(default='en attente', max_length=50)),
                ('acheteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achats', to=settings.AUTH_USER_MODEL)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestions.article')),
            ],
        ),
    ]
