from operator import mod
from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.
# models.py

class City(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	province = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Person(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
	def __str__(self):
		return self.name

class Book(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	author = models.ForeignKey(
		Person,
		on_delete=models.CASCADE
	)

	def __str__(self):
		return self.title

class BookImage(models.Model):
	img = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.img