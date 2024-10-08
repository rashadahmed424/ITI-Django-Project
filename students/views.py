from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from students.models import students
# Create your views here.
class liststudents(ListView):
    model=students
    template_name='students_index.html'
    context_object_name='students'