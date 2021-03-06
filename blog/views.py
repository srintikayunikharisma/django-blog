from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class PostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = "home.html"
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin, DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/' #balik ke home

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

@login_required
def home_view(request):
	context = {}

	post = Post.objects.all()
	context["posts"] = post

	return render(request,"home.html",context)

@login_required
def about_view(request):
	context = {}

	context["nama"] = "Srintika"
	context["asal"] = "Bukittinggi"
	context["tinggi"] = "154"
	context["bb"] = "43"
	
	return render(request,"about.html",context)