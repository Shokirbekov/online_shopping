# Generated by Django 4.1.5 on 2023-03-10 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0006_alter_wishes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savat',
            name='wish',
        ),
    ]
