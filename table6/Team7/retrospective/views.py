from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from retrospective.models import *

questions = []

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'retrospective/login.html', context_dict)

def manager_set_up_form(request):
    return render(request,'retrospective/manager_set_up_form.html',{})

def logout_view(request):
    logout(request)

def meeting(request):
    return render(request,"retrospective/meeting.html",{})

def loginUser(request):
    username = request.POST['login_username']
    password = request.POST['login_password']
    user = authenticate(username=username, password=password)
    if user:
        return render(request,"retrospective/dashboard.html",{})
    else:
        return HttpResponse()


def memberForm(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    r=Retrospective.objects.filter(name='Doing Hackathon')
    print r[0].name
    item_list=Item.objects.all()
    poll_list=PollEntry.objects.all()
    context_dict={'item_list' : item_list , 'poll_list' : poll_list, 'name': r[0].name, 'team': r[0].team.name}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'retrospective/member_form.html', context_dict)


def addQuestion(request):
    questions += request.POST["question"]
    print questions