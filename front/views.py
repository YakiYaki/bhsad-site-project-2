from django.shortcuts import render
from front.data import artists


# Create your views here.


def index(request):
    return render(request, "index.html", {'lang': 'ru', 'artists_half1': artists[:(len(artists) // 2)],
                                                        'artists_half2': artists[(len(artists) // 2):]})


def ru(request):
    return render(request, "index.html", {'lang': 'ru', 'artists_half1': artists[:(len(artists) // 2)],
                                                        'artists_half2': artists[(len(artists) // 2):]})


def en(request):
    return render(request, "index.html", {'lang': 'en', 'artists_half1': artists[:(len(artists) // 2)],
                                                        'artists_half2': artists[(len(artists) // 2):]})
