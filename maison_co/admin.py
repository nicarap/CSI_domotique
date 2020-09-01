from django.contrib import admin
from .models import *

class PieceAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'surface')
	list_filter = ('name', 'surface')
	ordering       = ('id','surface', )
	search_fields  = ('name', )

	fieldsets = (
			 # Fieldset 1 : meta-info (titre, auteur…)
		('Général', {
			'classes': ['extrapretty', ],
			'fields': ('name',)
		}),
		# Fieldset 2 : contenu de l'article
		('Contenu de la pièce', {
			'description': 'La surface en km²',
			'fields': ('surface',)
		}),
	)

	def apercu_maison(self, piece):

		""" 
		Retourne les 40 premiers caractères du contenu de l'article, 
		suivi de points de suspension si le texte est plus long. 
		"""
		return Truncator(piece).chars(40, truncate='...')

		# En-tête de notre colonne
	apercu_maison.short_description = 'Aperçu du nom de la piece'

class LumiereAdmin(admin.ModelAdmin):
	#list_display = ('name', 'piece', 'categorie', 'etat', 'fabricant' ,'communication')
	list_display = ('name', 'piece', 'etat', 'fabricant' ,'communication', 'id')
	ordering       = ('id', 'name' )
	search_fields  = ('name', 'piece', 'etat', 'fabricant')

	fieldsets = (
			 # Fieldset 1 : meta-info (titre, auteur…)
		('Général', {
			'classes': ['extrapretty', ],
			'fields': ('name',)
		}),
		# Fieldset 2 : contenu de l'article
		('Description de la lumière', {
			'fields': ('piece', 'etat', 'fabricant', 'communication')
		}),
	)

class PriseCoAdmin(admin.ModelAdmin):
	list_display = ('name', 'piece', 'etat', 'fabricant' ,'communication')
	ordering       = ('id', 'name' )
	search_fields  = ('name', 'piece', 'etat', 'fabricant')

	fieldsets = (
			 # Fieldset 1 : meta-info (titre, auteur…)
		('Général', {
			'classes': ['extrapretty', ],
			'fields': ('name',)
		}),
		# Fieldset 2 : contenu de l'article
		('Description de la prise', {
			'fields': ('piece', 'etat', 'fabricant', 'communication')
		}),
	)

class CameraAdmin(admin.ModelAdmin):
	list_display = ('name', 'piece', 'etat', 'fabricant' ,'communication')
	ordering       = ('id', 'name' )
	search_fields  = ('name', 'piece', 'etat', 'fabricant')

	fieldsets = (
			 # Fieldset 1 : meta-info (titre, auteur…)
		('Général', {
			'classes': ['extrapretty', ],
			'fields': ('name',)
		}),
		# Fieldset 2 : contenu de l'article
		('Description de la prise', {
			'fields': ('piece', 'etat', 'fabricant', 'communication')
		}),
	)


class UserAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'prenom', 'age','sexe')
	list_filter = ('name', 'date_DN','sexe','date_CR')
	ordering       = ('id','name', )
	search_fields  = ('name','prenom','sexe','date_CR','date_DN' )

	fieldsets = (
			 # Fieldset 1 : meta-info (titre, auteur…)
		('Général', {
			'classes': ['extrapretty', ],
			'fields': ('name','prenom','age')
		}),
		# Fieldset 2 : contenu de l'article
		('Création de la personne', {
			'description': 'Date de naissance',
			'fields': ('date_DN',)
		}),
	)

class ScenarioAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'action', 'evenement','piece', 'date_CR')
	list_filter = ('name', 'action','evenement')
	ordering       = ('piece', )
	search_fields  = ('name','action','evenement','piece')

	fieldsets = (
			 # Fieldset 1 : meta-info (titre, auteur…)
		('Général', {
			'classes': ['extrapretty', ],
			'fields': ('name','piece')
		}),
		# Fieldset 2 : contenu de l'article
		('Création du scénario', {
			'fields': ('action', 'lumiere','prise','evenement','commentaire',)
		}),
	)






admin.site.register(Piece, PieceAdmin)
admin.site.register(Lumiere, LumiereAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(PriseCo, PriseCoAdmin)
admin.site.register(Camera, CameraAdmin)
admin.site.register(Scenario, ScenarioAdmin)
