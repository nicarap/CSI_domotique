from django.urls 				import path
from . 							import views
from .views 					import lumUpdate
from django.conf.urls.static 	import static
from django.conf 				import settings
from django.conf.urls 			import url


urlpatterns = [
	path('', views.home, name='home-list'),
	path('home', views.home),
	path('Mymaison', views.Maison),
	path('MyLum', views.Lum),
	path('MyLum_on', views.lum_create, name='lum_create'),
	path('addRoom', views.room_create, name='addRoom'),
	path('MyLum/delete/<int:id>', views.LumDelete.as_view(), name='lumiere_delete'),
	path('MyLum/update/<str_>/<int:id_>/<etat>', views.lumUpdate, name='lumiere_update'),
	path('scenar', views.Scenar),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)