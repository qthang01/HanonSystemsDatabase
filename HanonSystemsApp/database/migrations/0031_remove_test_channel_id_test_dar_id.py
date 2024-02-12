# Generated by Django 4.2.9 on 2024-02-09 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0030_alter_test_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='channel_id',
        ),
        migrations.AddField(
            model_name='test',
            name='dar_id',
            field=models.ForeignKey(db_column='dar_id', default=2, on_delete=django.db.models.deletion.CASCADE, to='database.dar', verbose_name='DAR'),
            preserve_default=False,
        ),
    ]
