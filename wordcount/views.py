from django.http import HttpResponse
from django.shortcuts import render


def home(req):
    return render(req, 'home.html', {
        'name': "Aaron"
    })


def count(req):
    print(req.GET)

    wordcount = {}

    for word in req.GET['fulltext'].split():
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    return render(req, 'count.html', {
        'data': len(req.GET['fulltext'].split()),
        'original': req.GET['fulltext'],
        'dict': wordcount.items()
    })
