# Generated by Django 2.2.6 on 2020-03-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_payroll_employee_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='paid',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]