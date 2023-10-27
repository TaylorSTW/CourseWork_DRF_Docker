# Generated by Django 4.2.4 on 2023-08-25 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0018_improve_crontab_helptext'),
        ('habits', '0004_rename_lead_time_in_seconds_habit_duration_in_seconds'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReminderTask',
            fields=[
                ('periodictask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_celery_beat.periodictask')),
                ('habit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='привычка')),
            ],
            options={
                'verbose_name': 'напоминание',
                'verbose_name_plural': 'напоминания',
            },
            bases=('django_celery_beat.periodictask',),
        ),
    ]