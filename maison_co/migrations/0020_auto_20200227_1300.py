# Generated by Django 3.0.2 on 2020-02-27 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maison_co', '0019_scenario_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='lumiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='maison_co.Lumiere'),
        ),
        migrations.AddField(
            model_name='scenario',
            name='prise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='maison_co.PriseCo'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='piece',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='maison_co.Piece'),
            preserve_default=False,
        ),
    ]
