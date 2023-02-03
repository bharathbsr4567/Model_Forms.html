from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def insert_topic(request):
    TFMO=TopicForm()
    d={'form':TFMO}
    if request.method=="POST":
        FD=TopicForm(request.POST)
        if FD.is_valid():
            FD.save()
        return HttpResponse('topic data inserted succesfully')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFMO=WebpageForm()
    d={'form':WFMO}
    if request.method=="POST":
        FD=WebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('Webpage data inserted Succesfully')

    return render(request,'insert_webpage.html',d)

def insert_accesrecords(request):
    AFMO=AccessrecordsForm()
    d={'form':AFMO}
    if request.method=="POST":
        FD=AccessrecordsForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('inserted data succesfully')
    return render(request,'insert_accesrecords.html',d)