# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello');

def create(request):
    return HttpResponse('create');

def read(request, id):
    return HttpResponse('read'+id);