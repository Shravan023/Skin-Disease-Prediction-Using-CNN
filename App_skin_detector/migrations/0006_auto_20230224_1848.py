# Generated by Django 3.2.18 on 2023-02-24 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_skin_detector', '0005_doctor_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctor_details',
            new_name='Doctor_detail',
        ),
        migrations.RemoveField(
            model_name='feedback_details',
            name='country',
        ),
    ]