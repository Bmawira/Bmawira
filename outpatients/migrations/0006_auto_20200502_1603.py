# Generated by Django 3.0.5 on 2020-05-02 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outpatients', '0005_outpatient_triage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalinfo',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='patient_vitals', to='outpatients.Outpatient'),
        ),
    ]
