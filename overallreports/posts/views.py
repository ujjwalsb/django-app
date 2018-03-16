# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.contrib import messages
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list":queryset,
		"title":"List"
	}
	return render(request, "index.html", context)
	# return HttpResponse("<h1>List</h1")

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# Success Message
		messages.success(request, "Successfully Created.")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Cannot Create !")
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# Success Message
		messages.success(request,"Successfully Updated.")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_delete(request):
	return HttpResponse("<h1>Delete</h1")