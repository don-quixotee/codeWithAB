from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class blogListView(ListView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/blogList.html'

    # def get_queryset(self):
    #     return Post.objects.filter(status='P')

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    