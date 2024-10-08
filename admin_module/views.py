from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from admin_module.models import books,students,borrowed_books
from admin_module.forms import booksform
# Create your views here.


def main(request):
    return render(request,'main.html')

    

class listbooks(ListView):
    model = books
    template_name = 'books_index.html'
    context_object_name = 'books'

class bookdetails(DetailView):
    model=books
    template_name='book_detail.html'
    context_object_name='book'

class bookdelete(DeleteView):
    model=books
    template_name='book_delete.html'
    success_url='/admin_module/books'

class bookedite(UpdateView):
    model=books
    template_name='book_edite.html'
    form_class= booksform

class bookcreate(CreateView):
    form_class=booksform
    template_name='book_create.html'
    model=books
    


    