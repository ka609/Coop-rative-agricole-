# Generated by Django 5.1.1 on 2024-11-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestions', '0004_article_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos_articles/'),
        ),
    ]
