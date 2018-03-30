from django.db import models

# Create your models here.
class  LinksTable(models.Model):
	topic = models.CharField(max_length = 200)
	title = models.CharField(max_length = 1000)
	link = models.CharField(max_length = 1000)

def __str__ (self):
	return '%s %s' % (self.title, self.topic)
