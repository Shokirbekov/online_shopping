# Generated by Django 4.1.5 on 2023-03-10 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyurtma', '0002_savat_user_wishes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
