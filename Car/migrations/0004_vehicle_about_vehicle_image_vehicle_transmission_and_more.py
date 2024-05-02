# Generated by Django 4.1.5 on 2024-05-01 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0003_vehicle_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='about',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='transmission',
            field=models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], default='automatic', max_length=20),
        ),
        migrations.DeleteModel(
            name='VehicleImage',
        ),
    ]