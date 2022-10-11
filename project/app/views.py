from django.shortcuts import render
from django.contrib.auth import logout


def logout(request):
    logout(request)
# Create your views here.
