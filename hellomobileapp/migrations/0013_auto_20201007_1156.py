# Generated by Django 3.1.1 on 2020-10-07 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hellomobileapp', '0012_auto_20201007_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportlist',
            old_name='devices',
            new_name='brand',
        ),
    ]
