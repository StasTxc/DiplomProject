# Generated by Django 3.2 on 2021-05-04 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]