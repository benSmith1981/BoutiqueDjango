# Generated by Django 3.0.1 on 2022-09-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220905_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
