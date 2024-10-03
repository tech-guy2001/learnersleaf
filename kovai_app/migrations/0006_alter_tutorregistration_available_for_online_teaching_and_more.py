# Generated by Django 4.1.1 on 2024-08-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kovai_app', '0005_tutorregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorregistration',
            name='available_for_online_teaching',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregistration',
            name='full_time_teacher',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregistration',
            name='help_with_homework',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregistration',
            name='willing_to_travel',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3, null=True),
        ),
    ]
