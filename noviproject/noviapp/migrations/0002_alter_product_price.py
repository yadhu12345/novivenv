# Generated by Django 4.2 on 2023-04-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noviapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
