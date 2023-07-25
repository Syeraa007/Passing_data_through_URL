from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def love(request,S):
    return HttpResponse(f'<center><h1><b>Hii..{S} ..!!We have a deal to complete it by this DAY</b></h1></center>')