# Generated by Django 2.2 on 2020-10-19 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assetdetails',
            old_name='host',
            new_name='asset',
        ),
    ]