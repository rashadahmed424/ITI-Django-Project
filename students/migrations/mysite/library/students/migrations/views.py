# views.py in library app

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Student, Borrow


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def admin_dashboard(request):
    books = Book.objects.all()
    students = Student.objects.all()
    borrowed_books = Borrow.objects.filter(returned=False)

    context = {
        'books': books,
        'students': students,
        'borrowed_books': borrowed_books
    }
    return render(request, 'library/admin_dashboard.html', context)


# views.py in library app

@user_passes_test(is_admin)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BookForm()

    return render(request, 'library/add_book.html', {'form': form})


@user_passes_test(is_admin)
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = BookForm(instance=book)

    return render(request, 'library/update_book.html', {'form': form})


@user_passes_test(is_admin)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('admin_dashboard')
# views.py

@user_passes_test(is_admin)
def search_student(request):
    query = request.GET.get('student_id')
    students = Student.objects.filter(student_id__icontains=query)
    return render(request, 'library/search_student.html', {'students': students})


@user_passes_test(is_admin)
def view_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    borrowed_books = Borrow.objects.filter(student=student, returned=False)

    return render(request, 'library/view_student.html', {'student': student, 'borrowed_books': borrowed_books})


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentRegistrationForm
from .models import Student


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Student.objects.create(user=user, student_id=f'STU{user.id}')
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentRegistrationForm()

    return render(request, 'library/register.html', {'form': form})
def view_books(request):
    books = Book.objects.all()
    return render(request, 'library/view_books.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})


from django.contrib.auth.decorators import login_required


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    student = Student.objects.get(user=request.user)

    if book.available:
        book.available = False
        book.save()
        Borrow.objects.create(student=student, book=book)

    return redirect('student_dashboard')


@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    borrowed_books = Borrow.objects.filter(student=student, returned=False)

    return render(request, 'library/student_dashboard.html', {'borrowed_books': borrowed_books})

#return book
@login_required
def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, id=borrow_id)
    borrow.returned = True
    borrow.book.available = True
    borrow.book.save()
    borrow.save()

    return redirect('student_dashboard')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('student_dashboard')
    else:
        form = StudentUpdateForm(instance=request.user)

    return render(request, 'library/update_profile.html', {'form': form})
