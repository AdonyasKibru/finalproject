# Generated by Django 5.0.6 on 2024-05-29 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_reservation_service_types_delete_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicetype',
            old_name='capacity',
            new_name='Number_Of_Attendees',
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='name',
            field=models.IntegerField(choices=[(1, 'Room'), (2, 'Pool')], default=1),
        ),
    ]