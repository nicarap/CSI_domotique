# Generated by Django 3.0.2 on 2020-01-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maison_co', '0003_delete_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='surface',
            field=models.CharField(default=50, max_length=100),
            preserve_default=False,
        ),
    ]