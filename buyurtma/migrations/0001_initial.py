# Generated by Django 4.1.5 on 2023-03-10 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asosiy', '0004_komment_sana_alter_komment_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
        migrations.CreateModel(
            name='Savat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soni', models.SmallIntegerField()),
                ('price', models.SmallIntegerField()),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('wish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.wishes')),
            ],
        ),
    ]