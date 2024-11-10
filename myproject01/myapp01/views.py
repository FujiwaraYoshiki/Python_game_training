from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'message': "Hello, dynamic world! This is a message from the view."
    }
    return render(request, 'myapp01/index.html', context)
