from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from core.views import CreateDatabase, SystemView, EditDatabase, SearchView
from .views import CreateUser

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name="home"),
    url(r'^create-user/$', CreateUser.as_view(), name='create_user'),
    url(r'^create-db/$', CreateDatabase.as_view(), name='create_database'),
    url(r'^create-db/(?P<id>\d+)/(?P<kind>meta)/$', CreateDatabase.as_view(), name='create_db_meta'),
    url(r'^db/(?P<slug>\w+)/$', SystemView.as_view(), name='system'),
    url(r'^db/(?P<slug>\w+)/edit/$', EditDatabase.as_view(), name='system_edit'),
    url(r'^search/$', SearchView.as_view(), name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)