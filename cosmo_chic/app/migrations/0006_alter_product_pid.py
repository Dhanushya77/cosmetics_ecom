# Generated by Django 5.1.4 on 2025-01-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.TextField(unique=True),
        ),
    ]