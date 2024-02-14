from django.shortcuts import render
from .models import Snack
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

# Create your views here.

class SnackListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
    context_object_name = 'snacks'

class SnackDetailView(DetailView):
    template_name = 'snacks_detail.html'
    model = Snack
    context_object_name = 'snack'
    
class SnackCreateView(CreateView):
    template_name = 'snacks_create.html'
    model = Snack
    context_object_name = 'snack'
    
class SnackUpdateView(UpdateView):
    template_name = 'snacks_update.html'
    model = Snack
    context_object_name = 'snack'
    
class SnackDeleteView(DeleteView):
    template_name = 'snacks_delete.html'
    model = Snack
    context_object_name = 'snack'