# Generated by Django 2.2.6 on 2020-04-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0005_boqsubitem_boq'),
    ]

    operations = [
        migrations.AddField(
            model_name='boq',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
    ]
