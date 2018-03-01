# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def post_list(request):
	return HttpResponse("<h1>List</h1")

def post_create(request):
	return HttpResponse("<h1>Create</h1")

def post_detail(request):
	return HttpResponse("<h1>Detail</h1")

def post_update(request):
	return HttpResponse("<h1>Update</h1")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1")