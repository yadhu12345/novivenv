# Generated by Django 4.2 on 2023-04-27 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noviapp', '0003_alter_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='item',
        ),
    ]