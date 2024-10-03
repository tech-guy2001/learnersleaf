# Generated by Django 4.1.1 on 2024-08-28 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kovai_app', '0020_message_sender_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorrequest',
            name='gender',
        ),
        migrations.AddField(
            model_name='requestpost',
            name='five_subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='requestpost',
            name='four_subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='requestpost',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('both', 'Both')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='requestpost',
            name='three_subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='requestpost',
            name='two_subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
