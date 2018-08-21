from django.shortcuts import render
from django.utils import timezone
from journal.forms import WriteOutForm, WriteDownForm


# Create your views here.
def index(request):
    if request.method == 'GET':
        date = timezone.now
        return render(request, 'index.html', {'date': date})


def content(request, val):
    if request.method == 'GET':
        return render(request, 'content.html', {'val': val})


def add(request):
    if request.method == 'GET':
        return render(request, 'journal/add/index.html', {})


def write_down(request):
    if request.method == 'GET':
        form = WriteDownForm()
        return render(request, 'journal/add/write-down.html', {'form': form})


def write_out(request):
    if request.method == 'GET':
        form = WriteOutForm()
        return render(request, 'journal/add/write-out.html', {'form': form})


def extra_write_out(request):
    if request.method == 'GET':
        return render(request, 'journal/add/extra-write-out.html', {})
