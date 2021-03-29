from django.shortcuts import render
from django.http import HttpResponse


def master(request):
    return render(request, 'main/master.html')