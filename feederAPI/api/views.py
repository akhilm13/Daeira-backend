from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import LinksTable
from .serializers import LinksTableSerializer
from .resources import LinksTableResource 
from .serializers import ArticleObject 

class LinksList(APIView):

	def get(self, request):
		#links = LinksTable.objects.all()
		resource = LinksTableResource()
		serializer = LinksTableSerializer(resource.getArticles('tech', 2), many=True)
		return Response(serializer.data)

	def post(self):
		pass




# Create your views here.
