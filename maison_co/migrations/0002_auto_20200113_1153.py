# Generated by Django 3.0.2 on 2020-01-13 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maison_co', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habitant',
            options={},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={},
        ),
        migrations.RemoveField(
            model_name='home',
            name='piece',
        ),
    ]