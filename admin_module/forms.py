from django import forms
from admin_module.models import books

class booksform(forms.ModelForm):
    class Meta:
        model =books
        fields= '__all__'


class searchform(forms.Form):
    student_id = forms.IntegerField(label='Student ID', required=True)


