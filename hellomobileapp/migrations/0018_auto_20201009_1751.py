# Generated by Django 3.1.1 on 2020-10-09 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hellomobileapp', '0017_auto_20201008_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportlist',
            old_name='code',
            new_name='status',
        ),
    ]
