from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail
import os
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect

def home(request):
	exo = EXOModel.objects.all()
	prog = programme.objects.order_by('prog')

	if request.method == 'POST':
		form = createExoFORM(request.POST)
		if form.is_valid():
			exo = form.save(commit=False)
			exo.nom = "LEBOOOOOOON"
			# try:
			# 	send_mail(exo.nom, exo.prenom, 'nicarap@hotmail.com', ['nicarap@hotmail.com'], fail_silently=False,)
			# except:
			# 	return HttpResponse('Invalid header found.')
			#send_mail(exo.nom, exo.prenom, 'nicarap@hotmail.com',['nicarap@hotmail.com'], fail_silently=False,)
			form.save()
			return HttpResponseRedirect('./home')
	else:
		form = createExoFORM()
	USER = os.getenv('USERNAME')
	return render(request, 'EXO/home.html', {'exo':exo, 'form':form, 'user':USER, 'prog':prog},)

def createEXO(request):
	if request.method == 'POST':
		form = createExoFORM(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('./home.html')
	else:
		form = createExoFORM()
	return render(request, 'EXO/createEXO.html', {'form':form})