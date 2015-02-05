# -*- coding: utf-8 -*-
# Adapted from <http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example>
from django import forms

CHOICES = [('NB', 'Naive Bayes'), ('LR', 'Logistic Regression')]

class DocumentForm(forms.Form):
    algorithm = forms.ChoiceField(choices=CHOICES)
    docfile = forms.FileField(label='')
