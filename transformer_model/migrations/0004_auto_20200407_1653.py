# Generated by Django 2.2.3 on 2020-04-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer_model', '0003_transformer_pba_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformer_pba',
            name='flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transformer_pba',
            name='impact',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
