# Generated by Django 4.1.5 on 2023-03-10 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0007_remove_savat_wish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savat',
            name='price',
        ),
    ]
