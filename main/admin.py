from django.contrib import admin

from main.models import Book, BookImage, City, Person

# Register your models here.
admin.site.register(Book)
admin.site.register(BookImage)
admin.site.register(Person)
admin.site.register(City)
