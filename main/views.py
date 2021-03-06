from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .serializers import Book, BookImageSerializer, BookSerializer, CitySerializer
from .models import Book, BookImage, City

def responseCreator(status = status.HTTP_200_OK, data = None, error = None):
    return Response({
					"data": data,
					"error": error,
				}, status=status)

def validateBody(request, attrs):
    for attr in attrs:
        res = request.data.get(attr)
        if res is None:
            return responseCreator(error="{} is required".format(attr), status=status.HTTP_404_NOT_FOUND)
    return None


@api_view(['GET'])
def all_books(request):
    all_books = Book.objects.select_related('author__hometown')
    serializer = BookSerializer(all_books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def books_by_title(request, title):
    book = Book.objects.select_related('author__hometown').filter(title__contains=title)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_city(request):
	if request.method == 'POST':
		isValid = validateBody(request, ['name', 'province'])
	if isValid != None:
		return isValid
	
	name = request.data.get("name")
	province = request.data.get("province")

	city = City.objects.create(
		name = name,
		province = province
	)
	return responseCreator(data=CitySerializer(city).data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_book(request):
	if request.method == 'POST':
		isValid = validateBody(request, ['title'])
	if isValid != None:
		return isValid
	
	title = request.data.get("title")
	# author = request.data.get("author")

	book = Book.objects.create(
		title = title,
	)
	return responseCreator(data=BookSerializer(book).data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def book(request, id):
	"""
	Handle CRUD Book.
    """
	if request.method == 'GET':
		try:
			book = Book.objects.get(id=id)
			serializer = BookSerializer(book, many=False).data
			return responseCreator(data=serializer, status=status.HTTP_200_OK)
		except ObjectDoesNotExist:
			return responseCreator(error="Book does not exist", status=status.HTTP_409_CONFLICT)
		

	if request.method == 'PUT':
		title = request.data.get("title")
		# author = request.data.get("author")

		book = Book.objects.get(id=id)
		if book is None:
			return responseCreator(error="Book does not exist", status=status.HTTP_409_CONFLICT)
		if title != None:
			book.title = title
		# if author != None:
		# 	book.author = author

		book.save()
		serializer = BookSerializer(book, many=False).data

		return responseCreator(data=serializer, status=status.HTTP_201_CREATED)
	
	if request.method == 'DELETE':
		try:
			book = Book.objects.get(id=id)
			msg = {
				'message': 
					str(book.id) + " - " + book.title + " is succesfully deleted"
				}
			book.delete()
			return responseCreator(data=msg, status=status.HTTP_200_OK)
		except ObjectDoesNotExist:
			return responseCreator(error="Book does not exist", status=status.HTTP_409_CONFLICT)

@api_view(['POST'])
def post_book_image(request):
	try:
		image = request.data['image']
		book_image = BookImage.objects.create(img=image)
		return responseCreator(data=BookImageSerializer(book_image).data, status=status.HTTP_201_CREATED)

	except KeyError:
		return responseCreator(error="Book does not exist", status=status.HTTP_409_CONFLICT)
