# Generated by Django 4.1.5 on 2023-02-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiserver', '0003_booking_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.FloatField(default=1),
        ),
    ]
