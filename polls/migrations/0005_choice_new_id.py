# Generated by Django 4.1 on 2023-02-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='new_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]