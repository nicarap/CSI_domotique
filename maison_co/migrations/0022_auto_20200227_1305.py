# Generated by Django 3.0.2 on 2020-02-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maison_co', '0021_auto_20200227_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenario',
            name='lumiere',
            field=models.CharField(max_length=100, null=True, verbose_name='Nom de la lumière'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='prise',
            field=models.CharField(max_length=100, null=True, verbose_name='Nom de la prise'),
        ),
    ]
