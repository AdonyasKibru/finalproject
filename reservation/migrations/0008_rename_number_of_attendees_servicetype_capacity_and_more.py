# Generated by Django 5.0.6 on 2024-05-29 02:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_remove_servicetype_name_servicetype_service_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicetype',
            old_name='Number_Of_Attendees',
            new_name='capacity',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='Service_Name',
        ),
        migrations.AddField(
            model_name='servicetype',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
