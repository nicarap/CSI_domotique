from django.urls 				import path
from . 							import views
from django.conf 				import settings
from django.conf.urls 			import url


urlpatterns = [
	path('', views.home, name='home-list'),
	path('EXO/home', views.home),
	path('EXO/createEXO', views.createEXO),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)C