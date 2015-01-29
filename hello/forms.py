# -*- coding: utf-8 -*-
# Adapted from <http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example>
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
