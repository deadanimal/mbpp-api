# Generated by Django 2.2.6 on 2021-02-27 07:38

import core.helpers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0039_auto_20210227_1538'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cert', models.FileField(null=True, upload_to=core.helpers.PathAndRename('mbpp-elatihan/certificates'))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('attendee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificate_attendee', to=settings.AUTH_USER_MODEL)),
                ('generated_by', models.ForeignKey(limit_choices_to={'user_type': 'TC'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificate_generated_by', to=settings.AUTH_USER_MODEL)),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificate_training', to='trainings.Training')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
