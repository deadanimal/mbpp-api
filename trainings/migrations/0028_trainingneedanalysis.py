# Generated by Django 2.2.6 on 2021-01-27 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainings', '0027_configuration_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingNeedAnalysis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('suggested_title', models.CharField(max_length=255, null=True)),
                ('suggested_facilitator', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('core', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='training_need_analysis_core', to='trainings.TrainingCore')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='training_need_analysis_staff', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
