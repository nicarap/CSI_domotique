from django import forms
from .models import *

class createExoFORM(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.fields['nom'].widget.attrs.update({'class':'form-control'})
		self.fields['test'].widget.attrs.update({'class':'form-control'})

	class Meta:
		model = EXOModel
		fields = ('__all__')