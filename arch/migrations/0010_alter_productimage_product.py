# Generated by Django 5.1.1 on 2025-01-17 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arch', '0009_alter_productimage_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='arch.products'),
        ),
    ]
