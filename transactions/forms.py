from django import forms
from .models import Farmer, Company, Transaction

class CreateFarmer(forms.ModelForm):

	class Meta:
		model: Farmer
		fields = '__all__'


class CreateCompany(forms.ModelForm):

	class Meta:
		model: Company
		fields = '__all__'


class CreateTransaction(forms.ModelForm):
	date = forms.DateTimeField(widget = forms.DateField)
	class Meta:
		model: Transaction
		fields = '__all__'
