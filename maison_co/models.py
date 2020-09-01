from django.db import models
from django.utils import timezone

class Piece(models.Model):
	name = models.CharField(max_length=100, verbose_name="Nom")
	surface = models.CharField(default=20,
								max_length=100)
	slug = models.SlugField(blank=True)

	def __str__(self):
		return self.name

	class Meta: 
		verbose_name = "Pièce"
		ordering = ['name']

class User_Common(models.Model):
    
	name = models.CharField(max_length=100, verbose_name="Nom")
	prenom = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	age = models.IntegerField()
	sexe = models.CharField(max_length=1)
	date_DN = models.DateTimeField(verbose_name="Date de naissance")
	date_CR = models.DateTimeField(default=timezone.now,
		verbose_name="Date de création")
	slug = models.SlugField(blank=True, max_length=100)
	CHOIX_DROIT = [
        (1, 'Administrateur'),
        (0, 'Utilisateur'),]
	droit = models.CharField(
        max_length=1,
        choices=CHOIX_DROIT,
        default=0,
    )
	#piece = models.ForeignKey('Piece', on_delete=model.CASCADE)

	class Meta:
		abstract = True

class ObjectConnect(models.Model):
	name = models.CharField(max_length=100)
	#CHOIX_CATEG = [
	#	('LUM', 'Lumière'),('PRISE', 'Prise'),('CAM', 'Camera'),]
	CHOIX_ETAT = [
		(0, 'Off'),
		(1, 'On'),]
	CHOIX_COMM = [
		('WF', 'WiFi'),('BT', 'BlueTooth'),]

	fabricant = models.CharField(max_length=100, default="unknwon")
	etat = models.IntegerField(choices=CHOIX_ETAT, default=0)
	#categorie = models.CharField(max_length=100, choices=CHOIX_CATEG)
	communication = models.CharField(max_length=100, choices=CHOIX_COMM, null=True)
	#add categorie pour configurer nouvel objet connecter ?
	class Meta:
		abstract = True

class User(User_Common):
	
	class Meta: 
		verbose_name = "Utilisateur"
		ordering = ['name']

	def __str__(self):
		return self.name

class Admin(User_Common):
	
	class Meta: 
		verbose_name = "Administrateur"
		ordering = ['name']

	def __str__(self):
		return self.name

class Lumiere(ObjectConnect):
	piece = models.ForeignKey('Piece', null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class PriseCo(ObjectConnect):
	piece = models.ForeignKey('Piece', null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class Camera(ObjectConnect):
	piece = models.ForeignKey('Piece', null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.name

class Scenario(models.Model):

	CHOIX_ACTION = [('on', 'Allumer'),('off', 'Eteindre'),]
	CHOIX_EVNT = [('mvt','Détecte un mouvement'),('abs','Si je ne suis pas là'),('h','A une heure précise')]

	name = models.CharField(max_length=100, verbose_name="Nom du scénario")
	date_CR = models.DateTimeField(default=timezone.now,
		verbose_name="Date de création")
	piece = models.ForeignKey('Piece', on_delete=models.CASCADE)
	lumiere = models.CharField(max_length=100, null=True, verbose_name="Nom de la lumière")
	prise = models.CharField(max_length=100, null=True, verbose_name="Nom de la prise")
	commentaire = models.CharField(max_length=100, verbose_name="Commentaire")


	action = models.CharField(
		max_length=100,
        choices=CHOIX_ACTION,
        default=0,
    )

	evenement = models.CharField(
		max_length=100,
        choices=CHOIX_EVNT,
        default=0,
    )

	class Meta: 
		verbose_name = "Scénario"
		ordering = ['name']