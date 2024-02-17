# Generated by Django 4.1.13 on 2024-02-16 15:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=1000000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='message_images/')),
                ('room', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=255)),
                ('date_of_journey', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('flight_number', models.CharField(max_length=20)),
                ('pnr_number', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('baggage_space', models.IntegerField()),
                ('is_checked', models.BooleanField(default=False)),
                ('baggage_number', models.CharField(max_length=5, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
