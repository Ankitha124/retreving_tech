from django.shortcuts import render
from app.models import *
from django.db.models.functions import*
# Create your views here.

def display_topics(request):
    topics=Topic.objects.all()
    topics=Topic.objects.filter(topic_name='cricket')
    topics=Topic.objects.exclude(topic_name='rugby')
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=WebPage.objects.all()
    webpages=WebPage.objects.filter(name='dhoni')
    webpages=WebPage.objects.exclude(name='virat')
    webpages=WebPage.objects.order_by('name')
    webpages=WebPage.objects.order_by('-name')
    webpages=WebPage.objects.order_by(Length('name'))
    webpages=WebPage.objects.order_by(Length('name').desc())
    d={'webpages':webpages}

    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    accessrecords=AccessRecords.objects.all()
    d={'accessrecords':accessrecords}

    return render(request,'display_accessrecords.html',d)