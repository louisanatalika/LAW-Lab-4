from django.db import models

# Create your models here.
# models.py
class Book(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)

class BookImage(models.Model):
	img = models.ImageField(upload_to='images/')
