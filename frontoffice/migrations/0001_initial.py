# Generated by Django 3.0.5 on 2020-05-05 11:04

from django.db import migrations, models
import django.db.models.deletion
import frontoffice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('id_card', models.CharField(max_length=300)),
                ('no_of_persons', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('intime', models.DateTimeField()),
                ('outtime', models.DateTimeField()),
                ('note', models.CharField(max_length=300)),
                ('document', models.ImageField(blank=True, upload_to=frontoffice.models.visitor_folder)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PostalReceive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_tile', models.CharField(max_length=300)),
                ('reference_no', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300)),
                ('to_title', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('document', models.ImageField(blank=True, upload_to=frontoffice.models.postal_receive_folder)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Postaldispatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_tile', models.CharField(max_length=300)),
                ('reference_no', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300)),
                ('from_title', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('document', models.ImageField(blank=True, upload_to=frontoffice.models.postal_dispatch_folder)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Phone_call_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.IntegerField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('description', models.CharField(max_length=300)),
                ('next_followup', models.DateField()),
                ('call_duration', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300)),
                ('call_type', models.CharField(max_length=300)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Equiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('next_followup', models.DateField()),
                ('assigned', models.CharField(max_length=300)),
                ('reference', models.CharField(max_length=300)),
                ('source', models.CharField(max_length=300)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Complain_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complain_type', models.CharField(max_length=300)),
                ('source', models.CharField(max_length=300)),
                ('complain_by', models.CharField(max_length=300)),
                ('phone', models.IntegerField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('description', models.CharField(max_length=300)),
                ('action_taken', models.CharField(max_length=300)),
                ('assigned', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300)),
                ('document', models.ImageField(blank=True, upload_to=frontoffice.models.complains_folder)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile')),
            ],
        ),
    ]