# Generated by Django 4.1.5 on 2024-05-01 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0002_vehicleimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
