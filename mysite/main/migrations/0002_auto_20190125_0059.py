# Generated by Django 2.1 on 2019-01-25 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkinglot',
            name='distance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='owner',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
