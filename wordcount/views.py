from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'home.html', {
        'name': "Aaron"
    })


def count(req):
    print(req.GET)
    return render(req, 'count.html', {
        'data': len(req.GET['fulltext'].split())
    })
