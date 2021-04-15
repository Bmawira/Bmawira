# Generated by Django 3.0.5 on 2020-05-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='Strength',
            new_name='strength',
        ),
        migrations.AddField(
            model_name='items',
            name='brand',
            field=models.CharField(blank=True, default='soft', max_length=300),
        ),
        migrations.AddField(
            model_name='items',
            name='status',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]