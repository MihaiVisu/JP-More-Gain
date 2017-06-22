from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'retrospective/index.html', context_dict)
=======
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
>>>>>>> a2b4d2358c0d8e0989d834c293dba6d0d9bfb2e3
