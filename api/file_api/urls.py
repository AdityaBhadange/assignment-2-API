from django.urls import path
from . import views

urlpatterns = [
	path("getnumbers/", views.GetNumbers.as_view()),
]