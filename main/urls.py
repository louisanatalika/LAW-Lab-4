from django.urls import path
from . import views

urlpatterns = [
	path('', views.all_books, name='all-books'),
	path('create/', views.create_book, name='create-book'),
    path('<int:id>/', views.book, name='book'),
	path('post-image/', views.post_book_image, name='create-book-image'),
]