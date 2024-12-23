from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def trimmer(request):
    template = loader.get_template('mainpage.html')
    return HttpResponse(template.render())