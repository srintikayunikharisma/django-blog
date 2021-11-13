from django.shortcuts import render

def home_view(request):
	context= {}

	return render(request,"home.html",context)

def about_view(request):
	context= {}

	return render(request,"about.html",context)
