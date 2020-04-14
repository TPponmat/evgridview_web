# Generated by Django 2.2.3 on 2020-04-07 14:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transformer_PBA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=15)),
                ('subtypecod', models.BigIntegerField()),
                ('op_volt', models.CharField(max_length=2)),
                ('facilityid', models.CharField(max_length=13)),
                ('phasedesig', models.BigIntegerField()),
                ('ratekva', models.FloatField()),
                ('circuitcou', models.IntegerField()),
                ('configurat', models.CharField(max_length=2)),
                ('owner', models.CharField(max_length=1)),
                ('presenttap', models.CharField(max_length=1)),
                ('customerty', models.CharField(max_length=1)),
                ('loadstatus', models.IntegerField()),
                ('phasea_kva', models.FloatField()),
                ('phaseb_kva', models.FloatField()),
                ('phasec_kva', models.FloatField()),
                ('capnum', models.IntegerField()),
                ('totalkvar', models.IntegerField()),
                ('lanum', models.IntegerField()),
                ('constructi', models.CharField(max_length=1)),
                ('location', models.CharField(max_length=50)),
                ('angle', models.FloatField()),
                ('labeltext', models.CharField(max_length=60)),
                ('transforme', models.IntegerField()),
                ('installati', models.IntegerField()),
                ('creationus', models.CharField(max_length=50)),
                ('datecreate', models.DateField()),
                ('lastuser', models.CharField(max_length=50)),
                ('datemodifi', models.DateField()),
                ('feederid', models.CharField(max_length=7)),
                ('feederid2', models.CharField(max_length=7)),
                ('feederinfo', models.BigIntegerField()),
                ('electrictr', models.BigIntegerField()),
                ('enabled', models.IntegerField()),
                ('wbs', models.CharField(max_length=55)),
                ('existingkw', models.FloatField()),
                ('existingkv', models.FloatField()),
                ('existing_1', models.FloatField()),
                ('workreques', models.CharField(max_length=20)),
                ('designid', models.CharField(max_length=20)),
                ('worklocati', models.CharField(max_length=20)),
                ('workflowst', models.BigIntegerField()),
                ('workfuncti', models.BigIntegerField()),
                ('designtext', models.CharField(max_length=100)),
                ('graphicdes', models.CharField(max_length=10)),
                ('numberofus', models.BigIntegerField()),
                ('attachment', models.CharField(max_length=254)),
                ('matrefno', models.CharField(max_length=30)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
    ]