# Generated by Django 4.1.5 on 2024-05-01 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0009_vehicle_vechile_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vechile_category',
        ),
    ]
