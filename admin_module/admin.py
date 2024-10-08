from django.contrib import admin
from admin_module.models import books,borrowed_books,students

# Register your models here.
admin.site.register(books)
admin.site.register(borrowed_books)
admin.site.register(students)

