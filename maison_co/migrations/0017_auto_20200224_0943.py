# Generated by Django 3.0.2 on 2020-02-24 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maison_co', '0016_remove_camera_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lumiere',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='priseco',
            name='categorie',
        ),
    ]
