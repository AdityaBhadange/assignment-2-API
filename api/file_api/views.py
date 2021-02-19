# from django.shortcuts import render
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
		serializer = FileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()

			result = serializer["upload"].value
			result = result.split("/")

			path = f"media/uploads/{result[3]}"

			file = open(path, "r")
			contents = file.read()
			the = contents.count("the")
			this = contents.count("this")
			there = contents.count("there")
			file.close()

			resp = {"the": the, "this": this, "there": there}


			return Response(resp, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		# Now opening and reading recently saved file for returning count of some strings

