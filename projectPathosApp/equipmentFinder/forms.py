from django.db import models
from django import forms
from django.forms import ModelForm, TextInput, Textarea,Select, ClearableFileInput
from django.utils.translation import gettext_lazy as _
from .models import equipSearchClass, addEquipmentClass


class equipSearchForm(ModelForm):
    class Meta:
        model = equipSearchClass
        fields = ['searchTag']

        widgets = {
            'searchTag': TextInput(attrs={'class': 'searchTextBox', 'value': 'Please enter equipment tag/name...'}),
        }

        labels = {
            'searchTag': _('')
        }

plant_location = [
    ('Intake Pump House', 'Intake Pump House'),
    ('GT1', 'GT1'),
    ('GT2', 'GT2'),
    ('GT3', 'GT3'),
    ('HRSG1', 'HRSG1'),
    ('HRSG2', 'HRSG2'),
    ('HRSG3', 'HRSG3'),
]

class addEquipmentForm(ModelForm):
    class Meta:
        model = addEquipmentClass
        fields = ['tagID','equipName','equipLocation','equipImage']
        widgets = {
            'tagID': TextInput(attrs={'class': 'textInputBox', 'value': 'Equipment Tag ID'}),
            'equipName': TextInput(attrs={'class': 'textInputBox', 'value': 'Equipment Name'}),
            'equipLocation': Select(attrs={'class': 'textInputBox'},choices=plant_location),
            'equipImage': ClearableFileInput(attrs={'class': 'addImageButton','multiple':'true'})

        }
        labels = {
            'tagID': _(''),
            'equipName': _(''),
            'equipLocation': _(''),
            'equipImage': _('')
        }

class addEquipmentFormDoc(ModelForm):
    class Meta:
        model = addEquipmentClass
        fields = ['equipFile']
        widgets = {
            'equipFile': ClearableFileInput(attrs={'id': 'addFileButton', 'multiple': True })
        }
        labels = {
            'equipFile': _('')
        }