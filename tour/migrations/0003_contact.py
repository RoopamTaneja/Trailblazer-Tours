# Generated by Django 4.1 on 2023-02-24 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_user_tour_no_of_days_tour_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]