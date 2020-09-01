from django.db import models

class EXOModel(models.Model):
	nom = models.CharField(max_length=100)
	page = models.IntegerField()
	test = models.CharField(max_length=100, blank=True)
	prog = models.ForeignKey('programme', on_delete=models.CASCADE)

	def __str__(self):
		return self.nom

	class Meta: 
		verbose_name = "EXO"
		ordering = ['nom']

class programme(models.Model):
	nom = models.CharField(max_length=100)
	heure = models.IntegerField()

	def __str__(self):
		return self.nom