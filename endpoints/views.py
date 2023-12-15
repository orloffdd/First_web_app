from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def healthz(request):
    if request.method == "GET":
        return HttpResponse("ok")

def test(request):
    if request.method == "GET":
        return HttpResponse(str(os.environ["TEST_DATA"]))