# Generated by Django 4.0.6 on 2023-04-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_brand_category_price_product_store_delete_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='url',
        ),
        migrations.AddField(
            model_name='price',
            name='product_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]