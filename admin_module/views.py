from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView
# Create your views here.


def main(request):
    return render(request,'main.html')




    