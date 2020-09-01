from django.contrib import admin
from .models import *

class ExoAdmin(admin.ModelAdmin):
	list_display = ('nom','page', 'test')
	list_filter = ('nom', )
	ordering       = ('id','nom', )
	search_fields  = ('nom', )

	fieldsets = (
			 # Fieldset 1 : meta-info (titre, auteur…)
		('Général', {
			'classes': ['extrapretty', ],
			'fields': ('nom','page')
		}),
		# Fieldset 2 : contenu de l'article
		('Contenu de la pièce', {
			'description': 'La surface en km²',
			'fields': ('test', 'prog')
		}),
	)
class programmeAdmin(admin.ModelAdmin):
	list_display = ('nom',)
	list_filter = ('nom', )
	ordering       = ('id','nom', )
	search_fields  = ('nom', )

	fieldsets = (
			 # Fieldset 1 : meta-info (titre, auteur…)
		('Général', {
			'classes': ['extrapretty', ],
			'fields': ('nom','heure')
		}),
	)

admin.site.register(EXOModel, ExoAdmin)
admin.site.register(programme, programmeAdmin)