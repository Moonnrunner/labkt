from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template
def home(request):
    return render(request, 'templates/static_handler.html')
def hello(request):
	return HttpResponse(u'Hello world!', content_type="text/plain")