# Generated by Django 4.1.5 on 2023-03-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0012_alter_wishes_mahsulot'),
    ]

    operations = [
        migrations.AddField(
            model_name='savat',
            name='wished',
            field=models.BooleanField(default=False),
        ),
    ]
