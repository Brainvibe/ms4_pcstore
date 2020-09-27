from django.shortcuts import render

# Create your views here.

""" View for home page """


def index(request):

    return render(request, 'home/index.html')
