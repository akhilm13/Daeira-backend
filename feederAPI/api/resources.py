from api.models import LinksTable
from bs4 import BeautifulSoup
import requests
from api.serializers import ArticleObject

class LinksTableResource:
	
	
	def fetchArticleFromDatabase(self,link, title_db):
		r = requests.get(link)
		data = r.text
		soup = BeautifulSoup(data, "html.parser")
		heading = soup.find('h1')
		#print(heading.text)
		article = soup.find('article')
		children = article.findChildren()
		
		articleText = ''
		for child in children:
			if (child.name == 'p'):
#				print(child.text)
				articleText+=child.text
			elif(child.name == 'h3'):
#				print(child.text)
				articleText+=(child.text+'\n')
			elif ('class' in child.attrs.keys()):
				if (child.attrs['class'] == ['str-body-list']):
					list_items = child.find('ul').find_all('li')
					for li in list_items:
#						print(li.text)
						articleText+=('~ '+li.text+'\n')

		articleObject = ArticleObject(title = title_db, article = articleText)
		return articleObject



	def getArticles(self,topicToGet, numberOfArticles):
		queryset = LinksTable.objects.filter(topic=topicToGet)
		
		fetched_articles = []
		for x in queryset:
			articleLink = x.link
			fetched_articles.append(self.fetchArticleFromDatabase(articleLink), x.title)

		#replace this with bs code to retrieve articles. 
		#make them into a json and send it to the get method 
		#return queryset;
		return fetched_articles
		