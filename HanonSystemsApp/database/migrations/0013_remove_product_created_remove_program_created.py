# Generated by Django 4.2.4 on 2024-05-30 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_alter_program_enterproj_id_alter_program_phase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
        migrations.RemoveField(
            model_name='program',
            name='created',
        ),
    ]