# Generated by Django 3.2.18 on 2023-02-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_skin_detector', '0004_rename_feedback_feedback_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('Gender', models.CharField(default=None, max_length=100, null=True)),
                ('Speciality', models.CharField(default=None, max_length=100, null=True)),
                ('Department', models.CharField(default=None, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Doctor_detail',
            },
        ),
    ]
