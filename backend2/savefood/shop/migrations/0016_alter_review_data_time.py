# Generated by Django 3.2 on 2021-06-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_review_data_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Время'),
        ),
    ]