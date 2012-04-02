from django.shortcuts import render_to_response
from django.http import Http404
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
