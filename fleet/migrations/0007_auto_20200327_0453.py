# Generated by Django 2.2.6 on 2020-03-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0006_auto_20200326_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelreserverefill',
            name='quantity',
            field=models.FloatField(blank=True),
        ),
    ]
