from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy


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


class EditBlogView(UpdateView):

    model = Blog

    template_name = 'edit_post.html'

    fields = ['title', 'body']

class DeleteBlogView(DeleteView):

    model = Blog

    template_name = 'delete_post.html'

    success_url = reverse_lazy('home')
