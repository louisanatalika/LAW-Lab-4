from rest_framework import serializers
from .models import Book, BookImage, City

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'
		depth = 2

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = '__all__'
