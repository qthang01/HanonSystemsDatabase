# Generated by Django 4.2.4 on 2024-03-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_datetimetest'),
    ]

    operations = [
        migrations.AddField(
            model_name='datetimetest',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='datetimetest',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]