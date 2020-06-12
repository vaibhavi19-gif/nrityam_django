from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
from django.views.generic import ListView, DetailView
from .models import Feedback



def home(request):
    return render(request, 'home.html')


def gallery(request):
    return render(request, 'gallery.html')


def blog(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def pure(request):
    return render(request, 'pure.html')


def semi(request):
    return render(request, 'semi.html')


def Bharatanatyam(request):
    return render(request,'Bharatanatyam.html')


def amudra(request):
    return render(request,'amudra.html')


def shloka(request):
    return render(request, 'shloka.html')


def styles(request):
    return render(request, '7styles.html')


def featureB(request):
    return render(request, 'featureB.html')


def prarambhik(request):
    return render(request,'prarambhik.html')


def feedback(request):
    feeds = Feedback.objects.filter()
    return render(request, 'feedback.html', {'feeds': feeds})


def feedback_upload(request):
    username = request.POST['username']
    email = request.POST['email']
    course = request.POST['style']
    rate = request.POST['RATE']
    need = request.POST['text']

    feed = Feedback.objects.create(Username = username,Email = email, Course = course, Rate = rate, Need = need)
    feed.save()
    feeds = Feedback.objects.filter()
    return render(request, 'feedback.html', {'feeds': feeds})

