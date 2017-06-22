from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate


def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'retrospective/login.html', context_dict)


def logout_view(request):
    logout(request)

def loginUser(request):
    print request
    username = request.POST['login_username']
    password = request.POST['login_password']
    user = authenticate(username=username, password=password)
    if user:
        return render(request,"retrospective/member_form.html",{})
    else:
        return HttpResponse()


def memberForm(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'retrospective/member_form.html', context_dict)