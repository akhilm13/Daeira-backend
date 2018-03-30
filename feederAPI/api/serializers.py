from rest_framework import serializers
from .models import LinksTable

class ArticleObject:
	def __init__ (self, title,article):
		self.title = title
		self.article = article 

class LinksTableSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=500)
	article = serializers.CharField(max_length=500000)


