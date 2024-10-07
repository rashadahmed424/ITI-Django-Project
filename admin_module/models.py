from django.db import models
from students.models import students
from django.utils import timezone
# Create your models here.

class books(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=100)
    image=models.ImageField(upload_to='books/images',null=True)
    total=models.IntegerField()
    available=models.IntegerField()

    def __str__(self) -> str:
        return self.title

class borrowed_books(models.Model):
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    student = models.ForeignKey(students,null=True, on_delete=models.SET_NULL,related_name='borrowed_books')
    borrow_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.student} borrowed {self.book}'







