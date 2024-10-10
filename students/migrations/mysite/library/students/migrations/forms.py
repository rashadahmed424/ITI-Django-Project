# forms.py in library app

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'available']
# forms.py in library app

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'available']




from django import forms
from django.contrib.auth.models import User
from .models import Student


class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
#update
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
