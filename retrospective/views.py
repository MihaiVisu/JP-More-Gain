from django.shortcuts import render
from django.contrib.auth import login, authenticate


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username, password)
    if user:
        return 'SUCCESS'
    else:
        return 'INCORRECT LOGIN'


def logout_view(request):
    logout(request)
