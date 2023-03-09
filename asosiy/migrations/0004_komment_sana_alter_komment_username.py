# Generated by Django 4.1.5 on 2023-03-07 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_myuser_city_myuser_country_myuser_gender_and_more'),
        ('asosiy', '0003_komment_mahsulot'),
    ]

    operations = [
        migrations.AddField(
            model_name='komment',
            name='sana',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='komment',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.myuser'),
        ),
    ]