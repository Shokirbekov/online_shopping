# Generated by Django 4.1.5 on 2023-03-12 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0014_alter_wishes_mahsulot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishes',
            name='mahsulot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyurtma.savat'),
        ),
    ]
