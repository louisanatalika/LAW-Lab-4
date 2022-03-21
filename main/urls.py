from django.urls import path
from . import views

urlpatterns = [
	path('', views.all_books, name='all-books'),
	path('create/', views.create_book, name='create-book'),
    path('<int:id>/', views.book, name='book'),
	path('post-image/', views.post_book_image, name='create-book-image'),
	path('create/city', views.create_city, name='create-city'),
	path('<str:title>/', views.books_by_title, name='get-books-by-title'),
]