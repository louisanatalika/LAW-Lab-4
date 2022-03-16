from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .serializers import Book, BookImageSerializer, BookSerializer
from .models import Book, BookImage

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
    all_books = Book.objects.all()
    serializer = BookSerializer(all_books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_book(request):
	if request.method == 'POST':
		isValid = validateBody(request, ['title', 'author'])
	if isValid != None:
		return isValid
	
	title = request.data.get("title")
	author = request.data.get("author")

	book = Book.objects.create(
		title = title,
		author = author
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
		author = request.data.get("author")

		book = Book.objects.get(id=id)
		if book is None:
			return responseCreator(error="Book does not exist", status=status.HTTP_409_CONFLICT)
		if title != None:
			book.title = title
		if author != None:
			book.author = author

		book.save()
		serializer = BookSerializer(book, many=False).data

		return responseCreator(data=serializer, status=status.HTTP_201_CREATED)
	
	if request.method == 'DELETE':
		try:
			book = Book.objects.get(id=id)
			msg = {
				'message': 
					str(book.id) + " - " + book.title + " - " + book.author + " is succesfully deleted"
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
