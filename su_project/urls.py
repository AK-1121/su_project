from django.conf.urls import patterns, include, url
from django.contrib import admin
import lists

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'su_project.views.home', name='home'),
    url(r'^lists/', include('lists.urls', namespace='lists')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
