# Generated by Django 4.2.1 on 2023-06-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_maxprice_product_rangeprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='caracteristiques',
            field=models.TextField(blank=True),
        ),
    ]
