# Generated by Django 4.1.1 on 2024-09-27 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kovai_app', '0029_tutorrequest_coin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorregistration',
            name='filename',
            field=models.CharField(blank=True, choices=[('online_teaching', 'Online teaching'), ('offline_teaching', 'Offline teaching'), ('full_time', 'Full Time'), ('part_time', 'Part Time'), ('both', 'Both')], max_length=500, null=True),
        ),
    ]
