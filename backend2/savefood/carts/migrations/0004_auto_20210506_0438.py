# Generated by Django 3.2 on 2021-05-06 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cartitem_total_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='total_item',
            new_name='total_price',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
    ]