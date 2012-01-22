from django.conf.urls.defaults import *
from django.contrib import admin

from coltrane.models import Entry

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	(r'^search/$', 'cms.search.views.search'),
	(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
				 { 'document_root': 'c:/djangoproject/tinymce/' }),
	(r'^weblog/$', 'coltrane.views.entries_index'),
	
	# Generic views
	(r'^weblog/', include('coltrane.urls')),
)