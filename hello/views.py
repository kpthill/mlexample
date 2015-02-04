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
    model = naive_bayes.train(docfile)
    hypothesis = Hypothesis.objects.create(alg='NB', params=json.dumps(model))
    hypothesis.save()

    return render(request, 'db.html', {'model': hypothesis.pk})

def predict(request):
    # results = naive_bayes.classify(Hypothesis.objects.get(request.GET.get("model")).params, request.GET.get("sample"));
    n = request.GET.get("model")
    hypo = Hypothesis.objects.get(pk=n)
    results = ""
    results = naive_bayes.classify(json.loads(hypo.params), request.GET.get("sample"));
    return HttpResponse(json.dumps({"method": request.method,
                                    "is ajax": request.is_ajax(),
                                    "model_num": request.GET.get("model"),
                                    "hypo": hypo.alg,
                                    "results": results,
                                    "sample": request.GET.get("sample")}))
