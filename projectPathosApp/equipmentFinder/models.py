from django.db import models
from django.db import connection
from django.core.files.storage import FileSystemStorage

class equipInfoClass(models.Model):
    name = models.CharField(max_length=200)
    tagNumber = models.CharField(max_length=200)

class equipSearchClass(models.Model):
    searchTag = models.CharField(max_length=90)

class addEquipmentClass(models.Model):
    tagID = models.CharField(max_length=85)
    equipName = models.CharField(max_length=85)
    equipLocation = models.CharField(max_length=85)
    equipImage = models.ImageField(max_length=300, upload_to='equipImages',blank=False)
    equipFile = models.FileField(max_length=300, upload_to='equipDocs',blank=True)