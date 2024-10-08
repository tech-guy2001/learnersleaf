# Generated by Django 4.1.1 on 2024-08-08 02:53

from django.db import migrations, models
import kovai_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('kovai_app', '0006_alter_tutorregistration_available_for_online_teaching_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorregistration',
            name='otp',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tutorregistration',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='tutorregistration',
            name='id_proof',
            field=models.FileField(blank=True, null=True, upload_to=kovai_app.models.upload_to),
        ),
        migrations.AlterField(
            model_name='tutorregistration',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=kovai_app.models.upload_to),
        ),
    ]
