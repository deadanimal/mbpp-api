# Generated by Django 2.2.6 on 2020-07-01 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='updated_at',
            new_name='modified_at',
        ),
    ]
