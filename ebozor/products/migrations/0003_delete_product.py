# Generated by Django 3.2.8 on 2024-06-19 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
