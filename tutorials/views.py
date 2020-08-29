from django.shortcuts import render
from .models import Topic , Tutorial
from django.views.generic import ListView, DetailView


# Create your views here.
class TutorialsListView(ListView):
    model = Tutorial
    template_name = 'tutorials/tuteList.html'
    context_object_name = 'tutes'

class TuteDetailView(DetailView):
    model = Tutorial
    template_name = 'tutorials/tuteDetail.html'
    context_object_name = 'tute'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        tute = self.get_object()
        topics = Topic.objects.filter(tutorial=tute)
        context['topics'] = topics
        return context
    