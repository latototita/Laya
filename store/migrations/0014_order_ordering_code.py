# Generated by Django 2.2.14 on 2022-01-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordering_code',
            field=models.CharField(default='', max_length=6),
        ),
    ]
