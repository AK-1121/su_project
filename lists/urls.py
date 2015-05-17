from django.conf.urls import patterns, url
from lists import views

urlpatterns = patterns('',
    url(r'^$', views.show_add_page, name='show_add_item'),
    url(r'^add/$', views.add_item, name='add_item'),
)
