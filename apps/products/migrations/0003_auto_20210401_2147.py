# Generated by Django 3.1.7 on 2021-04-01 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210326_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity_type',
            new_name='type',
        ),
    ]
