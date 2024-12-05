# Generated by Django 5.1.3 on 2024-12-05 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_age_user_bmi_user_experience_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_avg', models.IntegerField()),
                ('heart_max', models.IntegerField()),
                ('heart_rest', models.IntegerField()),
                ('workout_type', models.CharField(max_length=50)),
                ('session_duration', models.FloatField()),
                ('water_intake', models.FloatField()),
                ('calories_burned', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_sessions', to='api.user')),
            ],
            options={
                'db_table': 'workout_sessions',
                'ordering': ['-created_at'],
            },
        ),
    ]
