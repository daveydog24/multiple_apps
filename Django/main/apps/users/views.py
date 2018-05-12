from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = 'placeholder to later display all the list of users'
	return HttpResponse(response)

def new_user(request):
	return redirect('/register')

def register(request):
	response = 'placeholder for users to create a new user record'
	return HttpResponse(response)

def login(request):
	response = 'placeholder for users to login' 
	return HttpResponse(response)

