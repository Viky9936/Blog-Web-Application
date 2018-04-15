
from django.conf.urls import url, include
from django.contrib import admin
#from myapp1 import views

urlpatterns = [
	url(r'', include('myapp1.urls')),
    url(r'^admin/', admin.site.urls),
]
