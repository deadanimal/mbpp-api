# Generated by Django 2.2.6 on 2021-01-27 11:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0005_auto_20210127_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('code', models.CharField(max_length=100, null=True)),
                ('classification', models.CharField(choices=[('FKW', 'FAEDAH KEWANGAN'), ('PDP', 'PENGESAHAN DALAM PERKHIDMATAN'), ('PSL', 'PEPERIKSAAN PENINGKATAN SECARA LANTIKAN (PSL)'), ('NA', 'Not Available')], default='NA', max_length=3)),
                ('organiser', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['classification', 'title'],
            },
        ),
        migrations.AlterField(
            model_name='examattendee',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='examattendee',
            name='note',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='examattendee',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attendees', to='exams.Exam'),
        ),
    ]
