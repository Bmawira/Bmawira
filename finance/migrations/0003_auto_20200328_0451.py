# Generated by Django 2.2.6 on 2020-03-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_allowance_bank_bankbranch_deduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='allowance',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deduction',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
