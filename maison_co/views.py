from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, UpdateView, View, DeleteView
from django.utils import timezone
from django.urls import reverse
from maison_co import views
import datetime
from .models import *
from .forms import *
import json
import os
from django.core import serializers
from django.templatetags.static import static


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def home(request):

	""" Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
	myHome = Piece.objects.all()
	myUser = User.objects.all()
	myLum = Lumiere.objects.all()
	myCam = Camera.objects.all()
	myDate = datetime.date.today().strftime("%d/%m/%y")
	t_lum = {}
	t_cam = 0
	t_prise = 0
	#nb_item={{p.name, Lumiere.objects.filter(piece__pk=p.id)} for p in myHome}
	if myHome:
		for p in myHome: 
			t_lum[p] = (Lumiere.objects.filter(piece__pk=p.id).count(), PriseCo.objects.filter(piece__pk=p.id).count())
			t_cam = Camera.objects.filter(piece__pk=p.id).count()
			t_prise = PriseCo.objects.filter(piece__pk=p.id).count()

	
	return render(request, 'maison_co/dashboard.html', {
														'piece':myHome, 
														'user':myUser,
														'lum':myLum,
														'date':myDate,
														'cam':myCam,
														't_lum':t_lum,
														't_cam':t_cam,
														't_prise':t_prise,
															}
														)

def Maison(request):
	myHome = Piece.objects.all()
	myLum = Lumiere.objects.all()
	myPrise = PriseCo.objects.all()
	myCam = Camera.objects.all()
	return render(request, 'maison_co/Mymaison.html', {'piece':myHome, 'lum':myLum, 'prise':myPrise, 'cam':myCam})

def Lum(request):
	myLum = Lumiere.objects.order_by('piece')
	return render(request, 'maison_co/MyLum.html', {'lum':myLum})

def Scenar(request):

	if request.method == 'POST':
		form = ScenarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/scenar')
	else:
		form = ScenarioForm()


	myHome = Piece.objects.all()
	myLum = Lumiere.objects.all()
	myPrise = PriseCo.objects.all()
	myCam = Camera.objects.all()

	return render(request, 'maison_co/scenar.html', {'form': form, 'piece':myHome, 'lum':myLum, 'prise':myPrise, 'cam':myCam})
    
def lum_create(request):
    if request.method == 'POST':
        # si c'est une soumission de la form
        form = LumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/MyLum')
    else:
        # generation de la form initialement vide
        form = LumForm()

    # retour de la form, soit vide, soit remplie mais avec une erreur, avec un template
    return render(request, 'maison_co/MyLum_on.html', {'form': form})

def room_create(request):
    if request.method == 'POST':
        # si c'est une soumission de la form
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Mymaison')
    else:
        # generation de la form initialement vide
        form = RoomForm()

    # retour de la form, soit vide, soit remplie mais avec une erreur, avec un template
    return render(request, 'maison_co/addRoom.html', {'form': form})

def lumUpdate(request, str_, id_, etat):
	
	if str_ == "1":
		a = Lumiere.objects.get(id=id_)
		if a.etat:
			a.etat = 0
		else:
			a.etat = 1
		a.save() 
		# data = request.POST.get('data')
		data = {
			'Nom': a.piece.name,
			'Etat renseigne': a.etat,
			'STR' : str_
		}
		if data['Nom'] != "":
			data['Etat'] = a.etat
	else:
		a = Lumiere.objects.filter(piece__name=str_)
		for item in a:
			item.etat = etat
			item.save()
			data = {
				'Nom': item.name,
				'Etat renseigne': item.etat,
				'STR' : str_
			}
			data['Etat'] = item.etat
	# os.system('python3 maison_co/static/maison_co/script/searchphone.py')
	# os.system('python3 maison_co/static/maison_co/script/bip.py')
	return JsonResponse(data, safe=False)
	
class  LumDelete(DeleteView):
	template_name = 'maison_co/lumiere_delete.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Lumiere, id=id_)

	def get_success_url(self):
		return reverse(views.Lum)

#class  LumDelete(DeleteView):
#    def  post(self, request, id):
#        data =  dict()
 #       lum = Lumiere.objects.get(id=id)
#        if lum:
#            lum.delete()
#            data['message'] =  "Lum deleted!"
#        else:
 #           data['message'] =  "Error!"
#        return JsonResponse(data)


# class lumUpdate(UpdateView):
#     template_name = 'maison_co/lumiere_update.html'
#     form_class = LumForm
#     queryset = Lumiere.objects.all()
#     field = ['etat']

#     def get_object(self):
#     	id_ = self.kwargs.get("id")
#     	return get_object_or_404(Lumiere, id=id_)

#     def get_success_url(self):
#     	return reverse(views.Lum)