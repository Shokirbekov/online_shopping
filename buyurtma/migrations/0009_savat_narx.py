# Generated by Django 4.1.5 on 2023-03-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0008_remove_savat_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='savat',
            name='narx',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
