# Generated by Django 4.1.5 on 2024-05-01 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0004_vehicle_about_vehicle_image_vehicle_transmission_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='newest_car',
            field=models.BooleanField(default=False),
        ),
    ]