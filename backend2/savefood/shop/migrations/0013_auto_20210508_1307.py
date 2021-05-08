# Generated by Django 3.2 on 2021-05-08 10:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('data_time',)},
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='review',
            name='data_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
    ]
