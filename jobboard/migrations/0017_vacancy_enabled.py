# Generated by Django 2.0 on 2018-01-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0016_auto_20180117_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
