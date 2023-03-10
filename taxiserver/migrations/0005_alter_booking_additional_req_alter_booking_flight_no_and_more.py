# Generated by Django 4.1.5 on 2023-03-05 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiserver', '0004_booking_start_geo_ln'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='additional_req',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='flight_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name_board',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='passenger_firstname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='passenger_lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='passenger_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
