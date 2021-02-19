from django.shortcuts import render
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import File
from rest_framework import status
from .serializers import FileSerializer


class GetNumbers(APIView):
	parser_classes = [MultiPartParser, FormParser]

	def post(self, request, format=None):
		# print("######request.FILES[0]", request.FILES['file'])

		serializer = FileSerializer(data=request.data)
		print(serializer)
		if serializer.is_valid():
			print("serializer is valid")
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			
		# print(request.data['file'])
		if "file" not in request.data:
			raise ParseError("Empty content")

		# file_object = File(request.FILES["file"])
		# file_object.save()

		
		# f = open("media/uploads/text.txt", "r")
		# file_content = f.read()
		# print(file_content)
		# f.close()

		return Response({"Recieved data": request.FILES['file']})
