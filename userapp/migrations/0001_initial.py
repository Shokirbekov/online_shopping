# Generated by Django 4.1.5 on 2023-03-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=500)),
                ('l_name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
            ],
        ),
    ]
