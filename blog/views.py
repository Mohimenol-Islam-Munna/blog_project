from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Blog


class HomePage(ListView):

    model = Blog
    template_name = 'index.html'
    context_object_name = 'all_blog_posts'


class BlogDetailView(DetailView):

    model = Blog
    template_name ='post_detail.html'


class CreateBlogView(CreateView):

    model = Blog

    template_name = 'create_post.html'

    fields = ['title', 'author', 'body']