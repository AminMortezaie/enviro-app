# Generated by Django 5.0.6 on 2024-07-02 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordata',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='updated_at',
        ),
    ]
