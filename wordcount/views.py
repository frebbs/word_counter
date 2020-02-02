from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'home.html', {
        'name': "Aaron"
    })


def about(req):
    return HttpResponse('<h1>This is the about page</h1>')
