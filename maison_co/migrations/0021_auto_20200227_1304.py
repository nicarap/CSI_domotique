# Generated by Django 3.0.2 on 2020-02-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maison_co', '0020_auto_20200227_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenario',
            name='lumiere',
            field=models.CharField(default='a', max_length=100, verbose_name='Nom de la lumière'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scenario',
            name='prise',
            field=models.CharField(default='a', max_length=100, verbose_name='Nom de la prise'),
            preserve_default=False,
        ),
    ]
