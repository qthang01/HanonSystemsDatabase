# Generated by Django 4.2.4 on 2024-03-26 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_remove_test_dut_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_harness',
            name='date',
        ),
    ]
