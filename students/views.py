from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from students.models import students
# Create your views here.
class liststudents(ListView):
    model=students
    template_name='students_index.html'
    context_object_name='students'


def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST.get('phone')
        track = request.POST.get('track')
        address = request.POST.get('address')

        # Create a new student record
        student = students(name=name, email=email, phone=phone, track=track, address=address)
        student.save()

        # Redirect to a success page or display a success message
        return redirect('students.index')

    return render(request, 'students_signup.html')