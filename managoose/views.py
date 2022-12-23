import json
import uuid
import urllib
import datetime
import re 
import requests # for setting cookies

from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.utils import timezone
from django.contrib import auth
#from django.forms.util import ErrorList
from django.template.context import RequestContext
from django.shortcuts import render, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.core import serializers

import markdown
md = markdown.Markdown()

#import requests

from managoose.util import *
def simple_page(template):
	def handler(request):
		return renderWithNav(request, template)
	return handler


def search(request):
	return renderWithNav(request,"blog/"+blog)

def home(request):
	obj = {}
	obj['works'] = []
	obj['works'].append({
		"title" : "Secret VR Game",
		"background" : "",
		"position" : "Monkey Wizard",
		"link" : "",
		"date" : "Summer 2020",
        	"description" : "Early prototype. Magical powers of cube control. Written for Quest using Unity3D",
		"video" : { 
			"source": "https://player.vimeo.com/video/435624506", 
			"image" : "" 
		},
		"images" : [	
		],
	})
	return renderWithNav(request,'home.html', obj)

def search(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = FriendForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

