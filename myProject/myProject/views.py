from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse






def homePage(req):

    return render(req,'common/homePage.html')

def loginPage(req):

    return render(req,'common/loginPage.html')

def registerPage(req):

    return render(req,'common/registerPage.html')