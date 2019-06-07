# Generated by Django 2.2 on 2019-06-07 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.KERNEL_RESIDENCE_MODEL),
        migrations.swappable_dependency(settings.KERNEL_PERSON_MODEL),
        ('bhawan_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('designation', models.CharField(choices=[('aw', 'Assistant warden'), ('cw', 'Chief warden'), ('sup', 'Supervisor'), ('war', 'Warden'), ('waw', 'Warden wellness'), ('bscy', 'Bhawan secretary'), ('cscy', 'Cultural secretary'), ('mscy', 'Maintenance secretary'), ('mescy', 'Mess secretary'), ('sscy', 'Sports secretary'), ('tscy', 'Technical secretary')], max_length=5, unique=True)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_RESIDENCE_MODEL)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_PERSON_MODEL)),
            ],
            options={
                'verbose_name_plural': 'hostel contact',
            },
        ),
    ]
