# Generated by Django 2.2.3 on 2020-04-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transformer_pba',
            name='angle',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='capnum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='circuitcou',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='datecreate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='datemodifi',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='electrictr',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='enabled',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='existing_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='existingkv',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='existingkw',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='feederinfo',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='installati',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='lanum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='loadstatus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='numberofus',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='phasea_kva',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='phaseb_kva',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='phasec_kva',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='phasedesig',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='ratekva',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='subtypecod',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='totalkvar',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='transforme',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='workflowst',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transformer_pba',
            name='workfuncti',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
