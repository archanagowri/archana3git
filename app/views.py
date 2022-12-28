from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1><i><b><marquee><font color=green>God Is Really Great</font></marquee></b></i><h1>')