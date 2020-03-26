from django import forms
from .models import Farmer, Company, Transaction
from django.forms import DateTimeInput

class CreateFarmer(forms.ModelForm):

	class Meta:
		model = Farmer
		fields = '__all__'


class CreateCompany(forms.ModelForm):

	class Meta:
		model = Company
		fields = '__all__'

class MyDateInput(forms.DateTimeInput):
	input_type = 'date'

class TransactionForm(forms.ModelForm):

	class Meta:
		model = Transaction
		fields = '__all__'
		widgets = {
			'date' : MyDateInput()
		}

