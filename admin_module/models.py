from django.db import models
from students.models import students
from django.utils import timezone
from django.shortcuts import reverse 

# Create your models here.

class books(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=100)
    image=models.ImageField(upload_to='admin_module/books/images/',null=True)
    overview=models.TextField(default=None,max_length=300,null=True,blank=True)
    total=models.IntegerField()
    available=models.IntegerField()

    def __str__(self) -> str:
        return self.title

    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_url(self):
        url=reverse('book_details',args=[self.id])
        return url
    
    @property
    def delete_url(self):
        url=reverse('book_delete',args=[self.id])
        return url
    
    @property
    def edit_url(self):
        url=reverse('book_edit',args=[self.id])
        return url
    
    def get_absolute_url(self):
        url = reverse("book_details", args=[self.id])
        return url
    

class borrowed_books(models.Model):
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    student = models.ForeignKey(students,null=True, on_delete=models.CASCADE,related_name='borrowed_books')
    borrow_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.student} borrowed {self.book}'
    








