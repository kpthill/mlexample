from django.shortcuts import render
from django.http import HttpResponse

from .models import Hypothesis
from .forms import DocumentForm

import json

import naive_bayes
import logistic

algorithms = {"NB": naive_bayes, "LR": logistic}

def index(request):
    form = DocumentForm()
    return render(request, 'index.html', {'form': form})

def use(request):
    form = DocumentForm(request.POST, request.FILES)

    if not form.is_valid():
        return HttpResponse("Form response not valid.")

    docfile = request.FILES['docfile']
    alg_symbol = request.POST['algorithm']
    algorithm = algorithms[alg_symbol]
    model = algorithm.train(docfile)
    
    hypothesis = Hypothesis.objects.create(alg=alg_symbol, params=json.dumps(model))
    hypothesis.save()

    return render(request, 'db.html', {'model': hypothesis.pk})

def predict(request):
    n = request.GET.get("model")
    hypothesis = Hypothesis.objects.get(pk=n)
    alg = algorithms[hypothesis.alg]

    results = alg.classify(json.loads(hypothesis.params), request.GET.get("sample"));

    return HttpResponse(json.dumps({"results": results, "sample": request.GET.get("sample")}))
