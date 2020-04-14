# Generated by Django 2.2.3 on 2020-04-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer_model', '0002_auto_20200407_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transformer_PBA_Views',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilityid', models.CharField(max_length=13)),
                ('ratekva', models.FloatField(blank=True, null=True)),
                ('feederid', models.CharField(max_length=7)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
                ('impact', models.CharField(blank=True, max_length=500, null=True)),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
    ]