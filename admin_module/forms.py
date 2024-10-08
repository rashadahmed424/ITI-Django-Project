from django import forms
from admin_module.models import books


class booksform(forms.ModelForm):
    class Meta:
        model =books
        fields= '__all__'