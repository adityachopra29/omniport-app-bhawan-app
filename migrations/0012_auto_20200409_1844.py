# Generated by Django 2.2.3 on 2020-04-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhawan_app', '0011_complainttimeslot_hostel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roombooking',
            name='status',
            field=models.CharField(choices=[('apr', 'Approved'), ('pen', 'Pending'), ('rej', 'Rejected'), ('fwd', 'Forwarded'), ('cnf', 'Confirmed')], default='pen', max_length=10),
        ),
    ]
