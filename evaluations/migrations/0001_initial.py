# Generated by Django 2.2.6 on 2021-02-24 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainings', '0038_trainingabsencememo_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalEvaluation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer_1', models.CharField(max_length=1)),
                ('answer_2', models.CharField(max_length=1)),
                ('answer_3', models.CharField(max_length=1)),
                ('answer_4', models.CharField(max_length=1)),
                ('answer_5', models.TextField(null=True)),
                ('answer_6', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(limit_choices_to={'user_type': 'DH'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internal_evaluation_approved_by', to=settings.AUTH_USER_MODEL)),
                ('attendee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internal_evaluation_attendee', to=settings.AUTH_USER_MODEL)),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internal_evaluation_training', to='trainings.Training')),
                ('verified_by', models.ForeignKey(limit_choices_to={'user_type': 'TC'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internal_evaluation_verified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ExternalEvaluation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer_1', models.TextField()),
                ('answer_2', models.TextField()),
                ('answer_3', models.TextField()),
                ('answer_4', models.TextField()),
                ('answer_5', models.TextField()),
                ('answer_6', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('approved_by', models.ForeignKey(limit_choices_to={'user_type': 'DH'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='external_evaluation_approved_by', to=settings.AUTH_USER_MODEL)),
                ('attendee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='external_evaluation_attendee', to=settings.AUTH_USER_MODEL)),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='external_evaluation_training', to='trainings.Training')),
                ('verified_by', models.ForeignKey(limit_choices_to={'user_type': 'TC'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='external_evaluation_verified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ContentEvaluation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('topic_trainer', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=1)),
                ('presentation', models.CharField(max_length=1)),
                ('relevance', models.CharField(max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('evaluation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluation_training', to='evaluations.InternalEvaluation')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
