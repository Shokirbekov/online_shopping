# Generated by Django 4.1.5 on 2023-03-03 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('rasm', models.FileField(upload_to='bolimlar')),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('narx', models.PositiveIntegerField()),
                ('brend', models.CharField(max_length=500)),
                ('davlat', models.CharField(max_length=500)),
                ('kafolat', models.CharField(max_length=500)),
                ('min_miqdor', models.PositiveSmallIntegerField(default=1)),
                ('tasdiqlangan', models.BooleanField(default=True)),
                ('yetkazish', models.CharField(default='3-4 kun', max_length=500)),
                ('mavjud', models.BooleanField(default=True)),
                ('chegirma', models.PositiveIntegerField(default=0)),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.bolim')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
    ]
