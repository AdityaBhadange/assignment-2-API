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

			# Getting a file path after serialzing
			result = serializer["upload"].value
			result = result.split("/")
			path = f"media/uploads/{result[3]}"

			# Calling a file handling function for getting number of frequent words.
			response = parse_file(path)

			return Response(response, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def parse_file(path):
	"""
	This is function for opening, reading and counting frequent occurence of
	following words:
	["the", "this", "there"]
	"""
	try:
		file = open(path, "r")
		
		content = file.read()

		the = content.count("the ")
		this = content.count("this ")
		there = content.count("there ")

		file.close()

		response = {"the": the, "this": this, "there": there}
		return response

	except:
		response = {"error": "Could not read file"}
		return response
