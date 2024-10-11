from django.views.generic import ListView

from students.backends import User
from students.migrations.mysite.library.students.migrations.models import Student
from students.models import students
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
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


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Try to authenticate the user using the email
        try:
            user = Student.objects.get(email=email)  # Get user by email
            student = authenticate(request, username=user.username, password=password)  # Authenticate using username and password

            if student is not None:
                login(request, student)
                return redirect('/admin_module/books/')
            else:
                print("l,a;lmf;m")
                messages.error(request, 'Invalid password.')
        except User.DoesNotExist:
            messages.error(request, 'No user found with that email.')

    return render(request, 'students_login.html')
