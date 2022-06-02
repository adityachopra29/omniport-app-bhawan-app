# Generated by Django 3.2 on 2022-06-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhawan_app', '0012_room_studentaccommodation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='occupancy',
            field=models.CharField(choices=[('1', 'Single'), ('2', 'Double'), ('3', 'Triple')], default='1', max_length=15),
        ),
    ]
