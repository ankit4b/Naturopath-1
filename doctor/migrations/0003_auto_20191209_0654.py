# Generated by Django 2.2.7 on 2019-12-09 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20191208_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='fees',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='language',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='qualification',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
