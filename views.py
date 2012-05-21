from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('dateapp/current_datetime.html', locals())

def hours_ahead(request, hour_offset):
    try:
        hour_offset = int(hour_offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render_to_response('dateapp/hours_ahead.html', locals())

def display_meta(request):
    meta_values = request.META.items()
    meta_values.sort()
    return render_to_response('chap7app/diaplaymeta.html', locals())

