from django.shortcuts import render,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from admin_module.models import books,students,borrowed_books
from admin_module.forms import booksform,searchform
from django.contrib.auth.models import User 
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import  login_required





def main(request):
    return render(request,'main.html')


    
class listbooks(LoginRequiredMixin,ListView):
    model = books
    template_name = 'books_index.html'
    context_object_name = 'books'


class bookdetails(LoginRequiredMixin,DetailView):
    model=books
    template_name='book_detail.html'
    context_object_name='book'

class bookdelete(LoginRequiredMixin,DeleteView):
    model=books
    template_name='book_delete.html'
    success_url='/admin_module/books'

class bookedite(LoginRequiredMixin,UpdateView):
    model=books
    template_name='book_edite.html'
    form_class= booksform

class bookcreate(LoginRequiredMixin,CreateView):
    form_class=booksform
    template_name='book_create.html'
    model=books


class UpdatePass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_changed')  # Redirect to the new URL

class custompassupdate(LoginRequiredMixin,PasswordChangeDoneView):
    template_name='change_done.html'
    


@login_required
def search_student(request):
    form = searchform(request.GET or None)
    student = None

    if form.is_valid():
        student_id = form.cleaned_data.get('student_id')
        student = get_object_or_404(students, id=student_id)  
  

    return render(request, 'search_student.html', {'form': form, 'student': student})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')