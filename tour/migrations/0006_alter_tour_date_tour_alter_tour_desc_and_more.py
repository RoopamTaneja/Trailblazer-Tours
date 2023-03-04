# Generated by Django 4.1 on 2023-02-26 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='date_tour',
            field=models.DateField(default=datetime.date(2023, 2, 26)),
        ),
        migrations.AlterField(
            model_name='tour',
            name='desc',
            field=models.CharField(default='abc', max_length=500),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_name',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AlterField(
            model_name='tour',
            name='venue',
            field=models.CharField(default='abc', max_length=100),
        ),
    ]