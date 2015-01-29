from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .forms import DocumentForm

def index(request):
    form = DocumentForm()
    return render(request, 'index.html', {'form': form})

def use(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        docfile = request.FILES['docfile']
        cnt = 0;
        lines = []
        for line in docfile:
            lines.append(line)
            cnt = cnt + 1
            if cnt > 10:
                break

        return render(request, 'db.html', {'lines': lines})
