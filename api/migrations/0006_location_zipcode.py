# Generated by Django 4.2.8 on 2023-12-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_location_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='zipcode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
