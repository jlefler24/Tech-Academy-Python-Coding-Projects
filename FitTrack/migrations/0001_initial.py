# Generated by Django 2.2.5 on 2020-05-26 10:35

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('name', models.CharField(max_length=30)),
                ('exercises', models.CharField(choices=[('Bench Press', 'Bench Press'), ('Incline Bench Press', 'Incline Bench Press'), ('BB Bentover Row', ' BB Bentover Row'), ('Upright Row', 'Upright Row'), ('BB Curl', 'BB Curl'), ('DB Curl', 'DB Curl'), ('DIps', 'Dips'), ('Triceps Extention', 'Tricep Extention'), ('Back Squat', 'Back Squat'), ('Box Squat', 'Box Squat'), ('Romanian Deadlift', 'Romanian Deadlift'), ('Olympic Deadlift', 'Olympic Deadlift'), ('Military Press', 'Military Press'), ('Lateral Raise', 'Lateral Raise'), ('Sit-Ups', 'Sit-Ups'), ('Plank', 'Plank')], default='blank', max_length=30)),
                ('sets', models.PositiveSmallIntegerField(default=0)),
                ('reps', models.PositiveSmallIntegerField(default=0)),
                ('weight', models.PositiveSmallIntegerField(default=0)),
            ],
            managers=[
                ('Workouts', django.db.models.manager.Manager()),
            ],
        ),
    ]
