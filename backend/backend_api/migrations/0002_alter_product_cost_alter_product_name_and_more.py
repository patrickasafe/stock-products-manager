# Generated by Django 4.0.5 on 2022-06-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.FloatField(verbose_name='Cost Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Selling Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ref',
            field=models.CharField(max_length=9, verbose_name='Reference'),
        ),
    ]