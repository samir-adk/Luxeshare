# Generated by Django 4.1.5 on 2024-05-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
