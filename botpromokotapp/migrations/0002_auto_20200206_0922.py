# Generated by Django 3.0 on 2020-02-06 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botpromokotapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='cupons',
            old_name='campaign',
            new_name='campaigns',
        ),
    ]
