# Generated by Django 4.0.4 on 2022-07-31 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipmentFinder', '0003_alter_addequipmentclass_equipfile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addequipmentclass',
            name='equipFile',
            field=models.FileField(blank=True, max_length=300, upload_to='equipDocs'),
        ),
        migrations.AlterField(
            model_name='addequipmentclass',
            name='equipImage',
            field=models.ImageField(max_length=300, upload_to='equipImages'),
        ),
    ]
