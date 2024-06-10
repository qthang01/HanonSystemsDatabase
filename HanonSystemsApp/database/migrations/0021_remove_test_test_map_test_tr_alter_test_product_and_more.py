# Generated by Django 4.2.4 on 2024-06-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_remove_test_product_id_remove_test_test_map_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='test_map',
        ),
        migrations.AddField(
            model_name='test',
            name='tr',
            field=models.CharField(max_length=15, null=True, verbose_name='TR'),
        ),
        migrations.AlterField(
            model_name='test',
            name='product',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='testmap',
            name='tr',
            field=models.CharField(max_length=14, null=True, verbose_name='TR'),
        ),
    ]