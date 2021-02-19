from django.shortcuts import render
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView


class GetNumbers(APIView):
	parser_classes = [MultiPartParser, FormParser]

	def post(self, request, format=None):
		print("########### HELLO from POST Request")
		print("###########file data", request.data)
		print(request.data["file"])
		# if "file" not in request.data:
		# 	raise ParseError("Empty content")

		# f = request.data["file"]
		return Response({"Recieved data": request.data})
