# Generated by Django 2.2.6 on 2021-02-09 09:37

import core.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0037_auto_20210209_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingabsencememo',
            name='attachment',
            field=models.FileField(null=True, upload_to=core.helpers.PathAndRename('attachments')),
        ),
    ]
