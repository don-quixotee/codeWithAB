from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'Ab/home.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.all()[:4]
