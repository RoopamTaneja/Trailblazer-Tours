# Generated by Django 4.1 on 2023-03-03 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0013_tour_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='date_tour',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='no_of_days',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='venue',
        ),
    ]
