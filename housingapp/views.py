from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.db import transaction
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome_page(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login')
def details(request):
    return render(request, 'buying.html')
