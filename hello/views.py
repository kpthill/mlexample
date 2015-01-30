from django.shortcuts import render
from django.http import HttpResponse

from .models import Hypothesis
from .forms import DocumentForm

import naive_bayes
import json

def index(request):
    form = DocumentForm()
    return render(request, 'index.html', {'form': form})

def use(request):
    form = DocumentForm(request.POST, request.FILES)

    if not form.is_valid():
        return HttpResponse("Form response not valid.")

    docfile = request.FILES['docfile']
    model = naive_bayes.naive_bayes(docfile)
    hypothesis = Hypothesis.objects.create(alg='NB', params=json.dumps(model))
    hypothesis.save()

    return render(request, 'db.html', {'model': hypothesis.primary_key})
