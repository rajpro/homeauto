from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
	
	STATUS = (('6', 'Choose Status',), ('1', 'Active',),('0','Deactive'))
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}))
	status = forms.ChoiceField(required=True,choices=STATUS,widget=forms.Select(attrs={'class':'form-control'}))

	class Meta:
		model = Room
		fields = "__all__"