# Generated by Django 4.2.20 on 2025-03-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_page', '0002_alter_booking_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='room_label',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
