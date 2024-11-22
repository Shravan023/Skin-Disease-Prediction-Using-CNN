# Generated by Django 3.2.18 on 2023-02-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_skin_detector', '0006_auto_20230224_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicine_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(default=None, max_length=100, null=True)),
                ('medicine_on', models.CharField(default=None, max_length=100, null=True)),
                ('price', models.CharField(default=None, max_length=100, null=True)),
            ],
            options={
                'db_table': 'medicine_detail',
            },
        ),
    ]
