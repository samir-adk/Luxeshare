# Generated by Django 4.1.5 on 2024-05-01 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0005_vehicle_newest_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vechile_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vechile_category', to='Car.carcompany'),
        ),
    ]
