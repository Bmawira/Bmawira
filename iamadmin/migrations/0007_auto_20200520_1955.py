# Generated by Django 3.0.5 on 2020-05-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamadmin', '0006_auto_20200508_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.IntegerField(default='254'),
        ),
    ]
