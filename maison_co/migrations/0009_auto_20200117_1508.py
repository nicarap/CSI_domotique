# Generated by Django 3.0.2 on 2020-01-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maison_co', '0008_auto_20200117_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nom'),
        ),
    ]
