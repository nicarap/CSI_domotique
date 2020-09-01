from django import forms
from .models import ObjectConnect
from .models import *
from .models import Lumiere

class LumForm(forms.ModelForm):
    class Meta:
        model = Lumiere
        fields = ('name','piece')
 
class RoomForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = ('name',)
 

class ScenarioForm(forms.ModelForm):

	class Meta: 
		model = Scenario
		fields = ('name','piece', 'lumiere','piece','action','evenement')
