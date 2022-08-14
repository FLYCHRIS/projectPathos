# Generated by Django 4.0.4 on 2022-07-15 10:46

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipmentFinder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addEquipmentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagID', models.CharField(max_length=90)),
                ('equipName', models.CharField(max_length=90)),
                ('equipLocation', models.CharField(max_length=90)),
                ('equipImage', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='static/addEquipment/media'), upload_to='')),
                ('equipFile', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='static/addEquipment/docs'), upload_to='')),
            ],
        ),
    ]