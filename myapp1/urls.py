from django.conf.urls import url
from . import views

urlpatterns = [
    
    
    #url(r'home^$', views.index, name='myapp1_index'),
    url(r'^category/(?P<category_slug>[\w-]+)/$',views.post_by_category,name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$',views.post_by_tag,name='post_by_tag'),
    url(r'^(?P<pk>\d+)/$',views.post_detail,name='post_detail'), #important step to take numerical url pattern by \d+ with name regular expression name as pk
    #using syntax (?P<name>pattern) here name of pattern is pk.
    url(r'^$', views.post_list, name='post_list')
]