# Generated by Django 4.2.4 on 2024-05-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_remove_laptop_ram_limit_laptop_dar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='supervisor_comments',
            field=models.CharField(max_length=4000, null=True),
        ),
    ]
