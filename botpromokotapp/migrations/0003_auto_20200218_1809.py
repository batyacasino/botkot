# Generated by Django 3.0 on 2020-02-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botpromokotapp', '0002_auto_20200206_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cupons',
            name='discount',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cupons',
            name='promocode',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='types',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]