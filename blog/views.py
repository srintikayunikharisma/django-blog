from django.shortcuts import render
from .models import Post

def home_view(request):
	context= {}

	post = Post.objects.all()
	context["posts"] = post

	return render(request,"home.html",context)

def about_view(request):
	context= {}
	context["nama"] = "Srintika"
	context["asal"] = "Bukitinggi"
	context["tinggi"] = "154"
	context["bb"] = "42"
	return render(request,"about.html",context)
