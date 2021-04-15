# Generated by Django 2.2.6 on 2020-04-11 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0008_auto_20200411_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='boqsubitem',
            name='boq_item_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='boq_class_items', to='pm.BoqItemClass'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boqsubitem',
            name='boq_main_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='boq_sub_item', to='pm.BoqItem'),
        ),
    ]
