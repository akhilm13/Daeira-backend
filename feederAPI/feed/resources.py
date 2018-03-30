from tastypie.resources import ModelResource
from api.models import LinksTable

class LinksTableResource (ModelResource):
	class Meta:
		queryset = LinksTable.objects.all()
		resoruce_name = 'links'
